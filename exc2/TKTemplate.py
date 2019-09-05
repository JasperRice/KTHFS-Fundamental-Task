from Tkinter import *
from random import randint
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import time
import threading

continuePlotting = False

def change_state():
    global continuePlotting
    if continuePlotting == True:
        continuePlotting = False
    else:
        continuePlotting = True


def data_points():
    f = open("data.txt", "w")
    for i in range(10):
        f.write(str(randint(0, 10))+'\n')
    f.close()

    f = open("data.txt", "r")
    data = f.readlines()
    f.close()

    l = []
    for i in range(len(data)):
        l.append(int(data[i].rstrip("\n")))
    return l

def main():
    # initialise a window.
    root = Tk()
    root.config(background='white')
    root.geometry("1000x700")

    label = Label(root, text="Data Visualization", bg = 'white').pack()

    fig = Figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.grid()

    graph = FigureCanvasTkAgg(fig, master=root)
    graph.get_tk_widget().pack(side="top",fill='both',expand=True)

    def plotter():
        while continuePlotting:
            ax.cla()
            ax.grid()
            dpts = data_points()
            ax.plot(range(10), dpts, marker='o', color='orange')
            graph.draw()
            time.sleep(1)

    def gui_handler():
        change_state()
        threading.Thread(target=plotter).start()

    start_button = Button(root, text="Start/Stop", command=gui_handler, bg="red", fg="white")
    start_button.pack()

    root.mainloop()

if __name__ == '__main__':
    main()
