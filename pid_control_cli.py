import control
import matplotlib.pyplot as plt
from typing import Any


# Get numerator and denominator coefficients from user
numerator_coefficients: Any = list(map(float, input("Enter numerator coefficients (separated by space): ").split()))
denominator_coefficients: Any = list(map(float, input("Enter denominator coefficients (separated by space): ").split()))

# Define transfer function of the system
sys = control.tf(numerator_coefficients, denominator_coefficients)

# Define the controller
K: Any = control.tf([1], [1])

# Create a closed loop system
cl_sys = control.feedback(K * sys)

# Get the poles of the closed loop system
poles = control.pole(cl_sys)

# Calculate the gain
Kp = -1 * poles[0]
Ki = -1 * poles[1]

print("Proportional gain:", Kp)
print("Integral gain:", Ki)

# Step response plot
t, y = control.step_response(sys)
plt.plot(t, y)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Step response")
plt.grid()
plt.show()
