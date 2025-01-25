import numpy as np
from numpy.typing import NDArray


class Qubits:
    def __init__(self, index: int, state: str = "z"):
        self.index = index
        self.state = self.initial_state(state)

    def initial_state(self, state: str = "z") -> NDArray:
        """
        Qubits: The fundamental units of quantum information analogous to classical bits in traditional computing.
                This methods creates a state vector that represents as an array.
                        ψ= [α]
                            [β]
                where 𝛼 and β are complex numbers.

        ```
        Args:
            initial_state (str, optional): The initial orientation of the array.
                                    Must be one of ["z", "x", "y"]. Defaults to "z".
        ```

        Returns:
            NDArray: vector array.
        Raises:
            ValueError: If the provided state is not "z", "x", or "y".
        """

        if state == "z":
            self.state = np.array(
                [[1 + 0j], [0 + 0j]], dtype=np.complex128
            )  # |0⟩ state
        elif state == "x":
            self.state = np.array([[1], [1]], dtype=np.complex128) / np.sqrt(
                2
            )  # |+⟩ state
        elif state == "y":
            self.state = np.array([[1], [1j]], dtype=np.complex128) / np.sqrt(
                2
            )  # |i⟩ state
        else:
            print(state)
            raise ValueError(
                f"Invalid initial value '{state}'. Must be 'x', 'y' or 'z'."
            )
        return self.state

    def get_state(self) -> np.ndarray:
        return self.state
