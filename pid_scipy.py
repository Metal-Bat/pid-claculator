import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


class PID:
    """This class is designed to calculate different aspects of pid
    such as proportional gain, integral gain or even showing output plot
    """

    def __init__(self, transfer_function) -> None:
        self.transfer_function: signal.TransferFunction = transfer_function

    def step_of_transfer_function(self) -> tuple:
        """

        Returns:
            tuple: _description_
        """
        return signal.step(self.transfer_function)

    def proportional_gain(self) -> float:
        """_summary_

        Returns:
            float: _description_
        """
        t, y = self.step_of_transfer_function()
        sse = y[-1] - 1
        R = sse / 1
        return R

    def integral_gain(self) -> float:
        """_summary_

        Returns:
            float: _description_
        """
        t, y = self.step_of_transfer_function()
        integral = np.trapz(y - 1, t)
        L = integral / 1
        return L

    def step_plot(self) -> None:
        t, y = self.step_of_transfer_function()
        plt.plot(t, y)
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.title("Step Response of Transfer Function")
        plt.grid()
        plt.show()
