pip install tk
from tkinter import *
    master = Tk()
    def close_window():
        print("hhhhhhh")
    button = Button(master, text = 'Click me', command = close_window)
    button.pack()
    mainloop()
