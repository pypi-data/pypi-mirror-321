from typing import List, Union, Callable
import numpy as np


class CalculatorInterface:
    """
    Interface for a quantum calculator that supports classical (CPU) and GPU computation.

    Attributes:
        qubits (int): Number of qubits in the quantum system.
        prep (str): Initialization state ('z' for |0>, 'x' for |+>, etc.).
        use_gpu (bool): Whether to enable GPU computation.
    """

    def __init__(self, qubits: int, prep: str = "z", use_gpu: bool = False):
        pass

    def gate_apply(self, gate: np.ndarray, target: List[int]) -> None:
        """
        Apply a gate to the quantum state.

        Args:
            gate (np.ndarray): The gate matrix to apply.
            target_qubits (List[int]): Indices of the qubits the gate acts on.
        """
        pass

    def initialize_state(self) -> np.ndarray:
        """
        Initialize the quantum state as a vector in the computational basis.

        Returns:
            np.ndarray: The initialized quantum state vector.
        """
        pass
