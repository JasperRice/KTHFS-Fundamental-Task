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


# Function to Draw
def _h_(t):
    return 3 * np.pi * np.exp(-_lambda_(t))

def _lambda_(t):
    return 5 * np.sin(2*np.pi*1*t)


# Function for FuncAnimation
def animate(i, ts, vs, t, n, dt):
    print(ts, vs, t, n, dt)

    ts.append(t)
    vs.append(_h_(t))

    ts = ts[-n:]
    vs = vs[-n:]
    t += dt

    axl.clear()
    axl.plot(ts, vs)


if __name__ == '__main__':
    PERIODIC_INTERVAL = 1
    n = 100
    t = 0.0
    dt = PERIODIC_INTERVAL / n

    ts = []
    vs = []

    G = GUI()
    ani = animation.FuncAnimation(fig, animate, fargs=(ts, vs, t, n, dt), blit=True, interval=5000)
    # ani.save("Exc2Demo.gif")
    G.mainloop()
