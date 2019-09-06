#!/usr/bin/env python
import matplotlib
matplotlib.use("TkAgg")

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import Tkinter as tk
import ttk
# import time
# import threading

from matplotlib.backends.backend_tkagg import FigureCanvasTk, FigureCanvasTkAgg, NavigationToolbar2Tk, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import style
style.use("ggplot")


f = Figure(figsize=(8, 8), dpi=100)
a = f.add_subplot(111)


def animate(i):
    pullData = open("sampleData.txt", "r").read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    for eachLine in dataList:
        if len(eachLine) > 1:
            x, y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))

    a.clear()
    a.plot(xList, yList)


class Top(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # tk.Tk.iconbitmap(self, default="DV.ico")
        tk.Tk.wm_title(self, "This is Title")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageGraph):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(PageGraph)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page")
        label.pack(padx=10, pady=10)

        button1 = ttk.Button(self, text="Page 1",
                            command=lambda:controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self, text="Page 2",
                            command=lambda:controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="Graph",
                            command=lambda:controller.show_frame(PageGraph))
        button3.pack()


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 1")
        label.pack(padx=10, pady=10)

        button1 = ttk.Button(self, text="Home",
                            command=lambda:controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page 2",
                            command=lambda:controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 2")
        label.pack(padx=10, pady=10)

        button1 = ttk.Button(self, text="Home",
                            command=lambda:controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Page 1",
                            command=lambda:controller.show_frame(PageOne))
        button2.pack()


class PageGraph(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph")
        label.pack(padx=10, pady=10)

        button1 = ttk.Button(self, text="Home",
                            command=lambda:controller.show_frame(StartPage))
        button1.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


if __name__ == '__main__':
    A = Top()
    ani = animation.FuncAnimation(f, animate, interval=1000)
    A.mainloop()
