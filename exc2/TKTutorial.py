#!/usr/bin/env python
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import Tkinter as tk
import ttk
# import time
# import threading


class Top(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self)

        tk.Tk.iconbitmap(self, default="clienticon.bmp")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

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


if __name__ == '__main__':
    A = Top()
    A.mainloop()
