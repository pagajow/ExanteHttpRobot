import numpy as np
import matplotlib.pyplot as plt


class Drawer:

    def test1(self):
        x = np.array([1, 2, 3, 4])
        y = np.array([11, 12, 13, 14])

        xr = np.flip(x)
        yr = np.flip(y)

        fig, ax = plt.subplots(2, 2)
        ax[0][0].plot(x, y)
        ax[1][1].plot(xr, yr)
        plt.show()
    def test2(self):
        x = np.array([1, 2, 3, 4])
        y = np.array([11, 12, 13, 14])

        fig = plt.Figure()
        ax1 = fig.add_subplot()
        ax1.plot(x, y)
        plt.show()


