#!/usr/bin/env python
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import Tkinter as tk
# import time
# import threading

class kthfsdv_exc2:
    PERIODIC_INTERVAL = 1
    n = 200
    t = 0

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    def __init__(self):
        print("Test: Class built.")
        self.dt = self.PERIODIC_INTERVAL / self.n
        self.ts = []
        self.vs = []

    def _h_(self):
        return 3 * np.pi * np.exp(-self._lambda_())

    def _lambda_(self):
        return 5 * np.sin(2*np.pi*1*self.t)

    # Called periodically by FuncAnimation
    def _update_(self, i):
        # Calculate and update value
        self.ts.append(self.t)
        self.vs.append(self._h_())
        self.t += self.dt

        # Limit lists to MAX_POINTS items
        self.ts = self.ts[-self.n:]
        self.vs = self.vs[-self.n:]

        # Plot
        self.ax.clear()
        self.ax.plot(self.ts, self.vs)

    def _plot_(self):
        animate = animation.FuncAnimation(self.fig,
                                          self._update_,
                                          fargs=self,
                                          interval=200)
        plt.title("Data Visualization")
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.grid()
        plt.show()

if __name__ == '__main__':
    A = kthfsdv_exc2()
    A._plot_()
