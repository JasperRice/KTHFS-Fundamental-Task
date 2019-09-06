#!/usr/bin/env python

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import Tkinter as tk
# import time
# import threading

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
style.use("ggplot")


# Called by FuncAnimation for Live Plotting
def animate(i, ts, vs, t):
    # Calculate and update value
    ts.append(self.t)
    vs.append(self._h_())
    self.t += self.dt

    # Limit lists to Max_POINTS items
    self.ts = self.ts[-self.n:]
    self.vs = self.vs[-self.n:]

    # Plot
    self.axl.clear()
    self.axl.plot(self.ts, self.vs)


class kthfsdv_exc2(tk.Tk):
    PERIODIC_INTERVAL = 1
    n = 100 # The maxlimum number of points

    fig = plt.figure()
    axl = fig.add_subplot(1, 1, 1)

    def __init__(self):
        print("Test: Class built.")

        tk.Tk.__init__(self)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)


        self.t = 0
        self.dt = self.PERIODIC_INTERVAL / self.n
        self.ts = []
        self.vs = []

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

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

        # Limit lists to Max_POINTS items
        self.ts = self.ts[-self.n:]
        self.vs = self.vs[-self.n:]

        # Plot
        self.axl.clear()
        self.axl.plot(self.ts, self.vs)

    def _plot_(self):
        ani = animation.FuncAnimation(self.fig,
                                          self._update_,
                                          # fargs=self,
                                          interval=200)
        plt.title("Data Visualization")
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.grid()
        plt.show()


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
        for F in (GraphPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Graph)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# Page of the Graph
class GraphPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        f = Figure(figsize=(5, 5), dpi=300)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8], [1,2,3,4,5,6,7,8])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


if __name__ == '__main__':
    A = GUI()
    A.mainloop()
