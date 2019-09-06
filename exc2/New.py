#!/usr/bin/env python
import matplotlib
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
matplotlib.use("TkAgg")
style.use("ggplot")

import numpy as np
import pandas as pd
import threading
import Tkinter as tk
import ttk


class exc2():
    T = 1.0
    N = 100
    NAME = ""

    def __init__(self):
        self.ts = []
        self.hs = []
        self.dt = self.T / self.N
        self.t  = 0
        self.STATE = False
        print("Class Created", self.T, self.N, self.ts, self.hs, self.dt, self.t)

    def _update_(self):
        self.ts.append(self.t)
        self.hs.append(self._h_())
        self.ts = self.ts[-self.N:]
        self.hs = self.hs[-self.N:]
        self.t += self.dt

    def _h_(self):
        return 3 * np.pi * np.exp(-self._lambda_())

    def _lambda_(self):
        return 5 * np.sin(2*np.pi*1*self.t)

    def _plot_(self):
        def animate():
            while self.STATE:
                axl.clear()
                axl.set_xlabel("Time")
                axl.set_ylabel("Value")
                # axl.grid()
                self._update_()
                axl.scatter(self.ts, self.hs, marker=".")
                canvas.draw()

        def name(Name):
            self.Name = Name

        def start():
            self.STATE = True
            threading.Thread(target=animate).start()

        def stop():
            self.STATE = False
            threading.Thread(target=animate).start()

        def reset():
            self.STATE = False
            self.__init__()
            threading.Thread(target=animate).start()

        def save():
            df = pd.DataFrame({'Time':self.ts, 'H':self.hs})
            df.to_csv("data.csv")


        fig = Figure(figsize=(8, 8), dpi=100)
        axl = fig.add_subplot(111)
        axl.set_xlabel("Time")
        axl.set_ylabel("Value")
        # axl.grid()

        root = tk.Tk()
        root.minsize(800, 800)
        root.wm_title("KTHFS: Data Visualization")
        # root.iconbitmap("DV.ico")

        experiment_name = ttk.Entry(root)
        experiment_name.grid(row=0, columnspan=3)

        name_button = ttk.Button(root, text="Enter Experiment Name")
        name_button.grid(row=0, column=3)

        start_button = ttk.Button(root, text="Start", command=start)
        start_button.grid(row=0, column=0)

        stop_button = ttk.Button(root, text="Stop", command=stop)
        stop_button.grid(row=0, column=1)

        reset_button = ttk.Button(root, text="Reset", command=reset)
        reset_button.grid(row=0, column=2)

        save_button = ttk.Button(root, text="Save") #, command=save)
        save_button.grid(row=0, column=3)

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, columnspan=4)
        # canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # toolbar = NavigationToolbar2Tk(canvas, root)
        # toolbar.update()
        # canvas._tkcanvas().grid(row=2, columnspan=4)
        # canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        root.mainloop()


if __name__ == '__main__':
    A = exc2()
    A._plot_()
