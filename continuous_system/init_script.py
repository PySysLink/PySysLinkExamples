import control


def second_order_state_space(wn, zeta):
    """Create a second-order transfer function and convert it to state space."""

    # G(s) = wn² / (s² + 2*zeta*wn*s + wn²)
    numerator = [wn**2]
    denominator = [1.0, 2.0 * zeta * wn, wn**2]

    transfer_function = control.tf(numerator, denominator)

    # Convert transfer function to state-space
    state_space = control.ss(transfer_function)

    return state_space


# Example
wn = 2.0
zeta = 0.7

system = second_order_state_space(wn, zeta)

A = system.A
B = system.B
C = system.C
D = system.D

print("A =", A)
print("B =", B)
print("C =", C)
print("D =", D)