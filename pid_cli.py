import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# Get user input for numerator and denominator coefficients
numerator_coefficients = list(map(int, input("Enter numerator coefficients separated by space: ").split()))
denominator_coefficients = list(map(int, input("Enter denominator coefficients separated by space: ").split()))

# Define the transfer function
sys = signal.TransferFunction(numerator_coefficients, denominator_coefficients)

# Simulate the step response
t, y = signal.step(sys)

# Calculate the steady-state error (SSE)
sse = y[-1] - 1

# Calculate the integral of the error over time
integral = np.trapz(y - 1, t)

# Calculate the proportional gain (R)
R = sse / 1

# Calculate the integral gain (L)
L = integral / 1

print(f"R: {R}, L: {L}")

# Plot the step response
plt.plot(t, y)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Step Response of Transfer Function")
plt.grid()
plt.show()
