'''from numpy import abs, around, multiply, square, log2, ndarray, isclose
from numpy.typing import NDArray
from typing import Union
from .base import convert_state
from ..quantum_circuit import QuantumCircuit


def probability(
    quantumstate=Union[ndarray, QuantumCircuit],
    round: int = None,
    show_percent: bool = False,
    show_bit: int = -1,
) -> NDArray:
    """
    Calculates the probability of measurement outcomes from a quantum state.

    Args:
        quantumstate (Union[ndarray, QuantumCircuit]): The quantum state to evaluate.
        show_percent (bool): Whether to return probabilities as percentages. Defaults to False.
        show_bit (int): Specific index to show probability for. Defaults to -1 (all probabilities).
        round (int): Rounds the probabilities to the specified number of decimal places.

    Returns:
        NDArray: Probability array for all states or a specific state.
    """
    quantum_state = convert_state(quantumstate)

    if round is not None and round < 0:
        return None
    circuit_size = int(log2(quantumstate.size))
    probabilities = abs(square(quantum_state))
    if show_bit >= 0:
        if show_bit >= 2**circuit_size:
            return None
        probabilities = probabilities[show_bit]
    if show_percent:
        probabilities = multiply(probabilities, 100)
    if not isclose(sum(probabilities), 1.0, atol=1e-6):
        return None
    return around(probabilities, decimals=round) if round is not None else probabilities
'''
