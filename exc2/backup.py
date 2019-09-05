#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import Tkinter as tk

class kthfsdv:
    f = 1

    def __init__(self):
        self.t = 0
        print(self._h_())

    def _h_(self):
        return 3 * np.pi * np.exp(-self._lambda_())

    def _lambda_(self):
        return 5 * np.sin(2*np.pi*1*self.t)



if __name__ == '__main__':
    BUTTON_WIDTH = 10
    BUTTON_HEIGHT = 2
    CANVAS_HEIGHT = 600
    CANVAS_WIDTH = 800

    root = tk.Tk()
    root.minsize(CANVAS_WIDTH, CANVAS_HEIGHT)

    # canvas = tk.Canvas(root, height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
    # canvas.pack()

    frame = tk.Frame(root, bg="grey")
    frame.place(height=CANVAS_HEIGHT, width=CANVAS_WIDTH-BUTTON_WIDTH)

    # control_buttons = tk.Listbox(root)

    start_button = tk.Button(
                        root,
                        text="Start",
                        activebackground="black",
                        activeforeground="white",
                        height=BUTTON_HEIGHT,
                        width=BUTTON_WIDTH
                    )
    start_button.pack()

    pause_button = tk.Button(
                        root,
                        text="Pause",
                        activebackground="black",
                        activeforeground="white",
                        height=BUTTON_HEIGHT,
                        width=BUTTON_WIDTH
                    )
    pause_button.pack()

    reset_button = tk.Button(
                        root,
                        text="Reset",
                        activebackground="black",
                        activeforeground="white",
                        height=BUTTON_HEIGHT,
                        width=BUTTON_WIDTH
                    )
    reset_button.pack()

    save_button = tk.Button(
                        root,
                        text="Save Figure",
                        activebackground="black",
                        activeforeground="white",
                        height=BUTTON_HEIGHT,
                        width=BUTTON_WIDTH
                    )
    save_button.pack()

    root.mainloop()
