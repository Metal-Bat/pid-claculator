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

P = 1.2 / abs(a)
Ti = 2 * abs(L)
Td = abs(L) / 2
Tp = 3.4 * abs(L)

values = f"a: {a}\nL: {L}\nP: {P}\nTi: {Ti}\nTd: {Td}\nTp: {Tp}\n"
print(values)

plt.style.use("cyberpunk")

figure, axis = plt.subplots(2)

plt.xlabel("Time (s)")
plt.ylabel("Output")
plt.title("Step Response of the system")

# Plot step response
first_axis = axis[0]
first_axis.plot(t, y)
first_axis.axvline(x=0, color="k")
first_axis.axhline(y=0, color="k")
# Add a line for the largest slope
first_axis.plot(t, slope * (t - t[i]) + y[i], "r--")
first_axis.legend(["Response", "Largest slope"])
# Plot point a and Annotate point a
first_axis.scatter(0, a, color="purple", marker=".", s=50)
first_axis.annotate("a", (0, a), textcoords="offset points", xytext=(-10, -2), ha="center")
# Plot point L and Annotate point L
first_axis.scatter(L, 0, color="green", marker=".", s=50)
first_axis.annotate("L", (L, 0), textcoords="offset points", xytext=(0, -10), ha="center")


# Plot the step response of the tuned transfer function with PID lines in axis[1]

pid_tf = control.tf(
    [P, P / Ti, P * Td],
    [1, 1 / Ti, Td],
)
t2, y2 = control.step_response(pid_tf * tf)

second_axis = axis[1]
second_axis.plot(t2, y2)
second_axis.axvline(x=0, color="k")
second_axis.axhline(y=0, color="k")
second_axis.set_xlabel("Time (s)")
second_axis.set_ylabel("Output")
second_axis.set_title("Tuned Step Response of the system")

mplcyberpunk.add_glow_effects()

plt.grid()
plt.show()
