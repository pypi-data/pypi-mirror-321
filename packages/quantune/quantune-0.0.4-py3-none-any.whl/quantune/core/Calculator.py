import numpy as np
from gates import *


class Reg:
    def __init__(self, n):
        self.n = n
        self.psi = np.zeros((2,) * n)
        self.psi[(0,) * n] = 1


def apply_gate(gate, qubit_index, reg):
    reg.psi = np.tensordot(gate(), reg.psi, (1, qubit_index))
    reg.psi = np.moveaxis(reg.psi, 0, qubit_index)


def parse_angle(angle_str):
    try:
        return eval(angle_str, {"pi": np.pi})
    except:
        raise ValueError("Invalid angle expression.")


def calculator():
    n = int(input("Enter the number of qubits: "))
    reg = Reg(n)

    while True:
        operation = input("Enter the operation name")

        if operation.lower() in [
            "h",
            "paulix",
            "pauliy",
            "pauliz",
            "s",
            "sdg",
            "t",
            "tdg",
            "sxdg",
        ]:
            i = int(input("Enter the qubit index: "))
            if operation.lower() == "h":
                apply_gate(hadamard, i, reg)
            elif operation.lower() == "paulix":
                apply_gate(paulix, i, reg)
            elif operation.lower() == "pauliy":
                apply_gate(pauliy, i, reg)
            elif operation.lower() == "pauliz":
                apply_gate(pauliz, i, reg)
            elif operation.lower() == "s":
                apply_gate(s, i, reg)
            elif operation.lower() == "sdg":
                apply_gate(sdg, i, reg)
            elif operation.lower() == "t":
                apply_gate(t, i, reg)
            elif operation.lower() == "tdg":
                apply_gate(tdg, i, reg)
            elif operation.lower() == "sxdg":
                apply_gate(sxdg, i, reg)

        elif operation.lower() == "cnot":
            control = int(input("Enter the control qubit index: "))
            target = int(input("Enter the target qubit index: "))
            cnot_matrix = cnot()
            cnot_tensor = np.reshape(cnot_matrix, (2, 2, 2, 2))
            reg.psi = np.tensordot(cnot_tensor, reg.psi, ((2, 3), (control, target)))
            reg.psi = np.moveaxis(reg.psi, (0, 1), (control, target))

        elif operation.lower() in ["rx", "ry", "rz", "r1", "phase"]:
            angle = input("Enter the rotation or phase angle: ")
            theta = parse_angle(angle)
            i = int(input("Enter the qubit index: "))

            if operation.lower() == "rx":
                apply_gate(rx(theta), i, reg)
            elif operation.lower() == "ry":
                apply_gate(ry(theta), i, reg)
            elif operation.lower() == "rz":
                apply_gate(rz(theta), i, reg)
            elif operation.lower() == "phase":
                apply_gate(phase(theta), i, reg)
            elif operation.lower() == "r1":
                apply_gate(r1(theta), i, reg)

        elif operation.lower == "u":
            i = int(input("Enter the qubit index: "))
            theta = input("Enter the rotation angle: ")
            theta = parse_angle(theta)
            phi = input("Enter the phase shift angle")
            phi = parse_angle(phi)
            lmbda = input("Enter the additional phase shift angle")
            lmbda = parse_angle(lmbda)
            apply_gate(u(theta, phi, lmbda), i, reg)

        elif operation.lower() == "swap":
            qubit1 = int(input("Enter the first qubit index: "))
            qubit2 = int(input("Enter the second qubit index: "))
            Swap_matrix = swap()
            Swap_tensor = np.reshape(Swap_matrix, (2, 2, 2, 2))
            reg.psi = np.tensordot(Swap_tensor, reg.psi, ((0, 1), (qubit1, qubit2)))
            reg.psi = np.moveaxis(reg.psi, (0, 1), (qubit1, qubit2))

        elif operation.lower() in ["rxx", "rzz"]:
            qubit1 = int(input("Enter the control qubit index: "))
            qubit2 = int(input("Enter the target qubit index: "))
            angle = input("Enter the rotation angle: ")
            theta = parse_angle(angle)

            if operation.lower() == "rxx":
                rxx_matrix = rxx(theta)
                rxx_tensor = np.reshape(rxx_matrix, (2, 2, 2, 2))
                reg.psi = np.tensordot(rxx_tensor, reg.psi, ((2, 3), (qubit1, qubit2)))
            else:
                rzz_matrix = rzz(theta)
                rzz_tensor = np.reshape(rzz_matrix, (2, 2, 2, 2))
                reg.psi = np.tensordot(rzz_tensor, reg.psi, ((2, 3), (qubit1, qubit2)))
            reg.psi = np.moveaxis(reg.psi, (0, 1), (qubit1, qubit2))
        elif operation.lower() == "print":
            print("Final State Vector:")
            print(reg.psi.flatten())
            break
        else:
            print("Invalid operation. Please try again.")


calculator()
