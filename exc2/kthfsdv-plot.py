#!/usr/bin/env python
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import Tkinter as tk
# import time
# import threading

from matplotlib import style
style.use("ggplot")


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


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page")
        label.pack(padx=10, pady=10)

        button1 = tk.Button(self, text="Visit Page 1",
                            command=lambda:controller.show_frame(PageOne))
        button1.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 1")
        label.pack(padx=10, pady=10)

        button2 = tk.Button(self, text="Back to Home",
                            command=lambda:controller.show_frame(StartPage))
        button2.pack()


if __name__ == '__main__':
    A = kthfsdv_exc2()
    print(A.ts)
    A._plot_()
    A.mainloop()
