from __future__ import annotations

import warnings
from functools import partial

import jax
import jax.numpy as jnp
from jaxtyping import Array, ArrayLike

from ..._checks import check_shape, check_times
from ...gradient import Gradient
from ...options import Options, check_options
from ...qarrays.dense_qarray import DenseQArray
from ...qarrays.qarray import QArrayLike
from ...result import MEPropagatorResult
from ...solver import Expm, Solver
from ...time_qarray import TimeQArray
from .._utils import (
    _astimeqarray,
    assert_solver_supported,
    cartesian_vmap,
    catch_xla_runtime_error,
    multi_vmap,
)
from ..core.expm_integrator import mepropagator_expm_integrator_constructor


def mepropagator(
    H: QArrayLike | TimeQArray,
    jump_ops: list[QArrayLike | TimeQArray],
    tsave: ArrayLike,
    *,
    solver: Solver = Expm(),  # noqa: B008
    gradient: Gradient | None = None,
    options: Options = Options(),  # noqa: B008
) -> MEPropagatorResult:
    r"""Compute the propagator of the Lindblad master equation.

    This function computes the propagator $\mathcal{U}(t)$ at time $t$ of the Lindblad
    master equation (with $\hbar=1$)
    $$
        \mathcal{U}(t) = \mathscr{T}\exp\left(\int_0^t\mathcal{L}(t')\dt'\right),
    $$
    where $\mathscr{T}$ is the time-ordering symbol and $\mathcal{L}$ is the system's
    Liouvillian. The formula simplifies to $\mathcal{U}(t)=e^{t\mathcal{L}}$ if the
    Liouvillian does not depend on time.

    Warning:
        This function only supports constant or piecewise constant Hamiltonians and jump
        operators. Support for arbitrary time dependence will be added soon.

    Note-: Defining a time-dependent Hamiltonian or jump operator
        If the Hamiltonian or the jump operators depend on time, they can be converted
        to time-qarrays using [`dq.pwc()`][dynamiqs.pwc],
        [`dq.modulated()`][dynamiqs.modulated], or
        [`dq.timecallable()`][dynamiqs.timecallable]. See the
        [Time-dependent operators](../../documentation/basics/time-dependent-operators.md)
        tutorial for more details.

    Note-: Running multiple simulations concurrently
        The Hamiltonian `H` and the jump operators `jump_ops` can be batched to compute
        multiple propagators concurrently. All other arguments are common to every
        batch. See the
        [Batching simulations](../../documentation/basics/batching-simulations.md)
        tutorial for more details.

    Args:
        H _(qarray-like or time-qarray of shape (...H, n, n))_: Hamiltonian.
        jump_ops _(list of qarray-like or time-qarray, each of shape (...Lk, n, n))_:
            List of jump operators.
        tsave _(array-like of shape (ntsave,))_: Times at which the propagators are
            saved. The equation is solved from `tsave[0]` to `tsave[-1]`, or from `t0`
            to `tsave[-1]` if `t0` is specified in `options`.
        solver: Solver for the integration. Defaults to
            [`dq.solver.Expm`][dynamiqs.solver.Expm] (explicit matrix exponentiation),
            which is the only supported solver for now.
        gradient: Algorithm used to compute the gradient. The default is
            solver-dependent, refer to the documentation of the chosen solver for more
            details.
        options: Generic options, see [`dq.Options`][dynamiqs.Options] (supported:
            `save_propagators`, `cartesian_batching`, `t0`, `save_extra`).

    Returns:
        [`dq.MEPropagatorResult`][dynamiqs.MEPropagatorResult] object holding
            the result of the propagator computation. Use the attribute
            `propagators` to access saved quantities, more details in
            [`dq.MEPropagatorResult`][dynamiqs.MEPropagatorResult].
    """  # noqa: E501
    # === convert arguments
    H = _astimeqarray(H)
    Ls = [_astimeqarray(L) for L in jump_ops]
    tsave = jnp.asarray(tsave)

    # === check arguments
    _check_mepropagator_args(H, Ls)
    tsave = check_times(tsave, 'tsave')
    check_options(options, 'mepropagator')

    # we implement the jitted vectorization in another function to pre-convert QuTiP
    # objects (which are not JIT-compatible) to qarrays
    return _vectorized_mepropagator(H, Ls, tsave, solver, gradient, options)


@catch_xla_runtime_error
@partial(jax.jit, static_argnames=('solver', 'gradient', 'options'))
def _vectorized_mepropagator(
    H: TimeQArray,
    Ls: list[TimeQArray],
    tsave: Array,
    solver: Solver,
    gradient: Gradient | None,
    options: Options,
) -> MEPropagatorResult:
    # vectorize input over H and Ls
    in_axes = (H.in_axes, [L.in_axes for L in Ls], None, None, None, None)
    out_axes = MEPropagatorResult.out_axes()

    if options.cartesian_batching:
        nvmap = (H.ndim - 2, [L.ndim - 2 for L in Ls], 0, 0, 0, 0)
        f = cartesian_vmap(_mepropagator, in_axes, out_axes, nvmap)
    else:
        bshape = jnp.broadcast_shapes(*[x.shape[:-2] for x in [H, *Ls]])
        nvmap = len(bshape)
        # broadcast all vectorized input to same shape
        n = H.shape[-1]
        H = H.broadcast_to(*bshape, n, n)
        Ls = [L.broadcast_to(*bshape, n, n) for L in Ls]
        # vectorize the function
        f = multi_vmap(_mepropagator, in_axes, out_axes, nvmap)

    return f(H, Ls, tsave, solver, gradient, options)


def _mepropagator(
    H: TimeQArray,
    Ls: list[TimeQArray],
    tsave: Array,
    solver: Solver,
    gradient: Gradient | None,
    options: Options,
) -> MEPropagatorResult:
    # === select integrator constructor
    integrator_constructors = {Expm: mepropagator_expm_integrator_constructor}
    assert_solver_supported(solver, integrator_constructors.keys())
    integrator_constructor = integrator_constructors[type(solver)]

    # === check gradient is supported
    solver.assert_supports_gradient(gradient)

    # === init integrator
    # todo: replace with vectorized utils constructor for eye
    data = jnp.eye(H.shape[-1] ** 2, dtype=H.dtype)
    # todo: timeqarray should expose dims without having to call at specific time
    y0 = DenseQArray(H(0.0).dims, True, data)
    integrator = integrator_constructor(
        ts=tsave,
        y0=y0,
        solver=solver,
        gradient=gradient,
        result_class=MEPropagatorResult,
        options=options,
        H=H,
        Ls=Ls,
    )

    # === run integrator
    result = integrator.run()

    # === return result
    return result  # noqa: RET504


def _check_mepropagator_args(H: TimeQArray, Ls: list[TimeQArray]):
    # === check H shape
    check_shape(H, 'H', '(..., n, n)', subs={'...': '...H'})

    # === check Ls shape
    for i, L in enumerate(Ls):
        check_shape(L, f'jump_ops[{i}]', '(..., n, n)', subs={'...': f'...L{i}'})

    if len(Ls) == 0:
        warnings.warn(
            'Argument `jump_ops` is an empty list, consider using `dq.sepropagator()`'
            ' to compute propagators for the Schrödinger equation.',
            stacklevel=2,
        )
