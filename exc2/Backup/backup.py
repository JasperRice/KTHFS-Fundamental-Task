#!/usr/bin/env python

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import Tkinter as tk
import ttk
# import time
# import threading

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
style.use("ggplot")


fig = plt.figure()
axl = fig.add_subplot(1, 1, 1)
plt.xlabel("Time")
plt.ylabel("Value")
plt.grid()


class kthfsdv_exc2:
    PERIODIC_INTERVAL = 1

    def __init__(self):
        print("Test: Class built.")
        self.t = 0
        self.n = 100
        self.dt = self.PERIODIC_INTERVAL / self.n
        self.ts = []
        self.vs = []

    def _h_(self):
        return 3 * np.pi * np.exp(-self._lambda_())

    def _lambda_(self):
        return 5 * np.sin(2*np.pi*1*self.t)

    # Called periodically by FuncAnimation
    def _update_(i, self):
        # Calculate and update value
        self.ts.append(self.t)
        self.vs.append(self._h_())
        self.t += self.dt

        # Limit lists to Max_POINTS items
        self.ts = self.ts[-self.n:]
        self.vs = self.vs[-self.n:]

        # Plot
        axl.clear()
        axl.plot(self.ts, self.vs)

        # Test
        print(self.ts)

    def _plot_(self):
        ani = animation.FuncAnimation(fig, self._update_, interval=1000)


# Graphic User Interface
class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "KTHFS: Data Visualization")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        self.frames = {}

        frame = GraphPage(container, self)
        self.frames[GraphPage] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(GraphPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# Page of the Graph
class GraphPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        start_button = ttk.Button(self, text="Start")
        start_button.pack()

        reset_button = ttk.Button(self, text="Reset")
        reset_button.pack()

        canvas = FigureCanvasTkAgg(fig, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


if __name__ == '__main__':
    G = GUI()
    A = kthfsdv_exc2()
    A._plot_()
    G.mainloop()
