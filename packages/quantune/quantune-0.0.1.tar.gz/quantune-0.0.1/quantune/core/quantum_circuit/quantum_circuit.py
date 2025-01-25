import subprocess
from ..qubit import QuantumRegister
from quantune.core.circuit_visualizer.visual import CircuitVisualizer
from ..tools import probability
import numpy as np
from ..quantum_gate import *
from ..circuit_visualizer import CircuitVisualizer
from .base import BaseCalculator
from .gpu import GpuCalculator
from ..quantum_gate import (
    hadamard,
    identity,
    paulix,
    pauliy,
    pauliz,
    phase,
    r1,
    rx,
    ry,
    rz,
    s,
    sdg,
    sx,
    sxdg,
    t,
    tdg,
    u,
)


class QuantumCircuit:
    def __init__(self, num_qubits: int, prep: str = "z", gpu: bool = False):
        self.num_qubits = num_qubits
        self.register = QuantumRegister(num_qubits)
        self.operations = []
        self.calculator = None
        self.gpu = gpu
        if prep != "z" and prep != "y" and prep != "x":
            raise ValueError("Qubit prep is not x,y,or z")
        if self.gpu:
            try:
                subprocess.check_output(["nvcc", "--version"]).decode()
            except FileNotFoundError:
                self.gpu = False
        if self.gpu:
            self.calculator = GpuCalculator(num_qubits, prep)
        else:
            self.calculator = BaseCalculator(num_qubits, prep)
        self.visualizer = CircuitVisualizer(self.num_qubits, self.operations)
        self.gpu = gpu
        self.circuit_info = {
            "num_qubits": num_qubits,
            "operations": [],
            "state_preparation": prep,
            "gpu": gpu,
        }

    def clear(self):
        """
        Clear all operations from the circuit.
        """
        self.operations = []
        self.circuit_info["operations"] = []

    def dump_circuit(self):
        """
        Dump the current circuit operations.

        Returns:
            list: List of operations in the circuit.
        """
        return self.operations

    def get_info(self):
        """
        Retrieve detailed information about the circuit.

        Returns:
            dict: Dictionary containing circuit information.
        """
        return self.circuit_info

    def add_gate(self, gate: np.ndarray, qubits: list[int], name: str) -> None:
        """
        Add a gate to the circuit.

        List of Gates you can add:
        -    Single-Qubit Gates:
        1. Identity
        2. H (Hadamard)
        3. Paulix
        4. Pauliy
        5. Pauliz
        6. S
        7. Sdg
        8. T
        9. Tdg
        10. Sxdg
        11. Sx
        12. Rx
        13. Ry
        14. Rz
        15. R1
        16. Phase
        17. U

        - `U` is a parametrized gate requiring three angles: `theta`, `phi`, and `lambda`.
        - `Rx`, `Ry`, `Rz`, `R1`, `Phase`, `CR`, `Rxx`, and `Rzz` require rotation or phase angles.


        Args:
            gate (ndarray): Matrix representation of the gate.
            qubits (list): List of qubits the gate acts on.
            name (str): Name of the gate for visualization purposes.
        """
        if not all(0 <= q < self.num_qubits for q in qubits):
            raise ValueError(f"Qubits {qubits} are out of range for this circuit.")
        self.operations.append((gate, qubits, name))

    def execute(self):
        """
        Execute the circuit by applying all gates in sequence to the quantum register.
        """
        for gate, qubits, _ in self.operations:
            print(f"Applying gate on qubits {qubits}: {gate}")
            self.calculator.gate_apply(gate, qubits)

        # Debug before synchronization
        print(f"Calculator state before synchronization: {self.calculator.state}")

        # Synchronize QuantumRegister state
        self.register.set_state(self.calculator.state)
        print(f"Final state in QuantumRegister: {self.register.get_state()}")

    def measure(self):
        """
        Measure the quantum register's final state and return probabilities.
        """
        final_state = self.register.get_state()
        print(f"Measuring final state: {final_state}")

        return probability(final_state)

    def draw_circuit(self, method: str = "text") -> None:
        """
        Visualize the quantum circuit.

        Args:
            method (str): Visualization method, either 'text' or 'matplotlib'. Defaults to 'text'.
        Raises:
            ValueError: If the method is not 'text' or 'matplotlib'.
        """
        viz_operations = [
            (gate, qubits, name) for gate, qubits, name in self.operations
        ]
        visualizer = CircuitVisualizer(self.num_qubits, viz_operations)

        if method.lower() == "text":
            print(visualizer.draw_text())
        elif method.lower() == "matplotlib":
            visualizer.draw_matplotlib()
        else:
            raise ValueError(
                "Invalid visualization method. Use 'text' or 'matplotlib'."
            )
