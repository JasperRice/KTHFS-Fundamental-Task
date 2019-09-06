#!/usr/bin/python

from math import pi, exp, sin
import pandas as pd
import Tkinter as tk
import matplotlib as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading


def lambda_func(t):
    return 5*sin(2*pi*1*t)


def h_func(t):
    return 3*pi*exp(-lambda_func(t))


class visualization():
    def __init__(self):
        self.t = []
        self.h = []
        self.lamda = []
        self.x = 0
        self.period = 0.01

        self.start_flag = False


    def add_new_data(self, x):
        t = x * self.period
        max_step = 1 / self.period
        if x <= max_step:
            self.t.append(t)
            self.lamda.append(lambda_func(t))
            self.h.append(h_func(t))
        else:
            self.t.pop(0) # discard old data
            self.lamda.pop(0)
            self.h.pop(0)
            self.t.append(t) # add new data
            self.lamda.append(lambda_func(t))
            self.h.append(h_func(t))


    def GUI(self):
        # Init canvas
        plt.use('TkAgg')
        top = tk.Tk()
        top.title("Visualization of Hongsheng Chang")

        fig = Figure(figsize=(10,4), dpi=100)
        a1 = fig.add_subplot(121)
        a1.set_xlabel('t')
        a1.set_ylabel('h')
        a1.grid()
        a2 = fig.add_subplot(122)
        a2.grid()
        a2.set_xlabel('t')
        a2.set_ylabel('lambda')

        canvas = FigureCanvasTkAgg(fig, master=top)
        canvas.get_tk_widget().grid(row=0, columnspan=3)

        def plot_fig():
            while self.start_flag:
                self.add_new_data(self.x )
                self.x += 1
                a1.cla()
                a2.cla()
                a1.grid()
                a2.grid()
                a1.set_xlabel('t')
                a1.set_ylabel('h')
                a2.set_xlabel('t')
                a2.set_ylabel('lambda')
                a1.scatter(self.t, self.h, s=50, c='b', marker='.')
                a2.scatter(self.t, self.lamda, s=50, c='r', marker='.')
                canvas.draw()


        def start_stop():
            if self.start_flag is False:
                print('Data collection running')
                self.start_flag = True
            else:
                print('Stop collection')
                self.start_flag = False
            threading.Thread(target = plot_fig).start()


        def reset():
            print('Reset figure')
            self.x = 0
            self.t = []
            self.lamda = []
            self.h = []


        def save():
            df = pd.DataFrame({'time':self.t,'h_value':self.h, 'lambda_value':self.lamda})
            df.to_csv('data.csv')

        # Init buttons
        start_button = tk.Button(top, text ="Start/Stop", command = start_stop).grid(row=1,column=0)
        reset_button = tk.Button(top, text ="Reset", command = reset).grid(row=1,column=1)
        save_button = tk.Button(top, text ="Save", command = save).grid(row=1,column=2)
        top.mainloop()


test = visualization()
test.GUI()
