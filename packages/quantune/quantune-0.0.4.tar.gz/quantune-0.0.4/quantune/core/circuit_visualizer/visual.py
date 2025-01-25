import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from ..quantum_gate import (
    hadamard,
    paulix,
    cnot,
)  # Importing gates from gates.py


class CircuitVisualizer:
    def __init__(self, num_qubits, operations):
        self.num_qubits = num_qubits
        self.operations = operations

    def draw_text(self):
        """
        Generate an improved text-based representation of the quantum circuit with connecting lines.
        """
        max_cols = (len(self.operations) + 1) * 2
        circuit = [["   " for _ in range(max_cols)] for _ in range(self.num_qubits)]

        for idx, (_, qubits, name) in enumerate(self.operations):
            if len(qubits) > 1:  # Multi-qubit gate
                control_qubit = qubits[0]
                target_qubit = qubits[1]

                # Add control and target markers
                circuit[control_qubit][idx * 2] = " ● "
                circuit[target_qubit][idx * 2] = " X "

                # Connect control and target qubits with vertical lines
                for q in range(
                    min(control_qubit, target_qubit) + 1,
                    max(control_qubit, target_qubit),
                ):
                    circuit[q][idx * 2] = " │ "

            else:  # Single-qubit gate
                circuit[qubits[0]][idx * 2] = f" {name} "

            # Add horizontal lines for all qubits
            for q in range(self.num_qubits):
                for col in range(max_cols):
                    if circuit[q][col] == "   ":
                        circuit[q][col] = " ─ "

        # Format the output with connecting lines
        text_output = ""
        for i, row in enumerate(circuit):
            text_output += f"q{i}: " + "".join(row) + "\n"
        return text_output

    def draw_matplotlib(self):
        """
        Generate an improved Matplotlib-based representation of the quantum circuit.
        """
        fig, ax = plt.subplots(figsize=(12, self.num_qubits + 1))
        ax.set_xlim(0, len(self.operations) + 1)
        ax.set_ylim(-0.5, self.num_qubits - 0.5)

        # Draw qubit lines
        for i in range(self.num_qubits):
            ax.hlines(
                y=i, xmin=0, xmax=len(self.operations), color="black", linestyle="-"
            )

        for idx, (_, qubits, name) in enumerate(self.operations):
            if len(qubits) > 1:  # Controlled gate
                control_qubit = qubits[0]
                target_qubit = qubits[1]

                # Draw control point
                ax.add_patch(
                    Circle((idx + 0.9, control_qubit), 0.1, color="red", zorder=3)
                )
                ax.text(
                    idx + 0.9,
                    control_qubit,
                    "+",
                    fontsize=14,
                    ha="center",
                    va="center",
                    color="white",
                    zorder=4,
                )

                # Draw target point with blue dot
                ax.add_patch(
                    Circle((idx + 0.9, target_qubit), 0.07, color="blue", zorder=3)
                )
                ax.plot(
                    [idx + 0.9, idx + 0.9],
                    [target_qubit, control_qubit],
                    color="black",
                    linestyle="-",
                    zorder=2,
                )

            else:  # Single-qubit gate
                for q in qubits:
                    ax.add_patch(
                        Rectangle(
                            (idx + 0.55, q - 0.2),
                            width=0.6,
                            height=0.4,
                            color="skyblue",
                            ec="black",
                            zorder=3,
                        )
                    )
                    ax.text(
                        idx + 0.85,
                        q,
                        name,
                        fontsize=10,
                        ha="center",
                        va="center",
                        zorder=4,
                    )

        # Configure axis labels
        ax.set_yticks(range(self.num_qubits))
        ax.set_yticklabels([f"q{i}" for i in range(self.num_qubits)])
        ax.set_xticks(range(len(self.operations) + 1))
        ax.set_xticklabels([""] * (len(self.operations) + 1))

        return fig
