import matplotlib.pyplot as plt
import control
import numpy as np
import mplcyberpunk

# Create transfer function
# Get user input for numerator and denominator coefficients
num = list(map(float, input("Enter numerator coefficients separated by space: ").split()))
den = list(map(float, input("Enter denominator coefficients separated by space: ").split()))
tf = control.tf(num, den)

# Simulate step response
t, y = control.step_response(tf)

# Find the largest slope of the response path
gradient = np.gradient(y, t)  # Calculate the derivative of the output with respect to time
slope = max(gradient)

# Find the location of the largest slope
i = np.argmax(gradient)

# Find point a
a = y[i] - slope * t[i]

# Find point L
L = -a / slope

P = 1.2 / a
Ti = 2 * L
Td = L / 2
Tp = 3.4 * L

values = f"a: {a}\nL: {L}\nP: {P}\nTi: {Ti}\nTd: {Td}\nTp: {Tp}\n"
print(values)

# Plot step response
plt.style.use("cyberpunk")

plt.plot(t, y)
plt.xlabel("Time (s)")
plt.ylabel("Output")
plt.title("Step Response of the system")
plt.axvline(x=0, color="k")
plt.axhline(y=0, color="k")

# Add a line for the largest slope
plt.plot(t, slope * (t - t[i]) + y[i], "r--")
plt.legend(["Response", "Largest slope"])

# Plot point a and Annotate point a
plt.scatter(0, a, color="purple", marker=".", s=50)
plt.annotate("a", (0, a), textcoords="offset points", xytext=(-10, -2), ha="center")

# Plot point L and Annotate point L
plt.scatter(L, 0, color="green", marker=".", s=50)
plt.annotate("L", (L, 0), textcoords="offset points", xytext=(0, -10), ha="center")

mplcyberpunk.add_glow_effects()

plt.grid()
plt.show()
