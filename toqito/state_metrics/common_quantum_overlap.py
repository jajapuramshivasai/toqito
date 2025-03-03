from toqito.state_opt.state_exclusion import state_exclusion
import numpy as np

def common_quantum_overlap(states: list[np.ndarray]) -> float:
    r"""
    Compute the common quantum overlap of a set of quantum states.
    
    The common quantum overlap of a set of quantum states :math:`\{ \rho_1, \ldots, \rho_n \}` is defined as
    """
    n = len(states)
    probs = [1] * n
    opt_val, _ = state_exclusion(vectors=states, probs=probs, primal_dual="dual")
    return n * (1 - opt_val)