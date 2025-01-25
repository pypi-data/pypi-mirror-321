import numpy as np
from quantum_gate.gates import *

class Reg:
    def __init__(self, n):
        self.n = n
        self.psi = np.zeros((2,)*n)
        self.psi[(0,)*n] = 1  

def apply_gate(gate, qubit_index, reg):
    reg.psi = np.tensordot(gate(), reg.psi, (1, qubit_index))  
    reg.psi = np.moveaxis(reg.psi, 0, qubit_index) 

def apply_gate_CT(gate_func, control, target, reg):
    gate_matrix = gate_func() if callable(gate_func) else gate_func
    gate_tensor = np.reshape(gate_matrix, (2, 2, 2, 2))
    reg.psi = np.tensordot(gate_tensor, reg.psi, ((2, 3), (control, target)))
    reg.psi = np.moveaxis(reg.psi, (0, 1), (control, target))

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

        if operation.lower() in ["identity", "h", "paulix", "pauliy", "pauliz", "s", "sdg", "t", "tdg", "sxdg", "sx"]:
            i = int(input(f"Enter the qubit index: "))
            if operation.lower() == "h":
                apply_gate(hadamard, i, reg)
            elif operation.lower() == "identity":
                apply_gate(identity, i, reg)   
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
            elif operation.lower() == "sx":
                apply_gate(sx, i, reg)             
            
        elif operation.lower() in ["cnot", "cz", "cr", "rxx", "rzz"]:
            control = int(input(f"Enter the control qubit index: "))
            target = int(input(f"Enter the target qubit index: "))

            if operation.lower() == "cnot":
                apply_gate_CT(cnot, control, target, reg)
            elif operation.lower() == "cz":
                apply_gate_CT(cz, control, target, reg)
            else:
                theta = input("Enter the rotation angle: ")
                theta = parse_angle(theta)
              if operation.lower() == "rxx":
                apply_gate_CT(rxx(theta), control, target, reg)
              elif operation.lower() == "rzz":
                apply_gate_CT(rzz(theta), control, target, reg)
              else:
                apply_gate_CT(cr(theta), control, target, reg)  
        
        elif operation.lower() in ["rx", "ry", "rz", "r1", "phase"]: 
            i = int(input(f"Enter the qubit index: "))
            angle = input("Enter the rotation or phase angle: ")
            theta = parse_angle(angle) 
            
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
            i = int(input(f"Enter the qubit index: "))
            theta = input("Enter the rotation angle: ")
            theta = parse_angle(theta)
            phi = input("Enter the phase shift angle")
            phi = parse_angle(phi)
            lmbda = input("Enter the additional phase shift angle")
            lmbda = parse_angle(lmbda)
            apply_gate(u(theta, phi, lmbda), i, reg)

        elif operation.lower() in ["swap", "toffoli"]:
            qubit1 = int(input(f"Enter the first qubit index: "))
            qubit2 = int(input(f"Enter the second qubit index: "))
            if operation.lower() == "swap":
              Swap_matrix = swap()  
              Swap_tensor = np.reshape(Swap_matrix, (2, 2, 2, 2))
              reg.psi = np.tensordot(Swap_tensor, reg.psi, ((0, 1), (qubit1, qubit2)))  
              reg.psi = np.moveaxis(reg.psi, (0, 1), (qubit1, qubit2))
            else:
              target = int(input(f"Enter the target qubit index: "))
              apply_gate_CT(toffoli, qubit1, qubit2, reg)   
      
        elif operation.lower() == "print":
            print("Final State Vector:")
            print(reg.psi.flatten())
            break
        else:
            print("Invalid operation. Please try again.")

calculator()
