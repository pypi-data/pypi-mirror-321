import numpy as np
from typing import Union


def convert_state(to_convert) -> np.ndarray:
    """
    Converts a given quantum state into a flattened ndarray.

    Args:
        to_convert (Union[QuantumCircuit, ndarray]): The state to convert.

    Returns:
        ndarray: Flattened and rounded quantum state.
    """
    from ...quantum_circuit import QuantumCircuit

    if isinstance(to_convert, QuantumCircuit):
        to_convert = to_convert.register.get_state()

    if not isinstance(to_convert, np.ndarray):
        raise TypeError("Input must be a QuantumCircuit or a numpy ndarray.")

    to_convert = to_convert.flatten()

    return np.around(to_convert, decimals=10)
