#!/bin/python

# Just some initial thingy

import tkinter as tk

# Main application window
class Application(tk.Frame):
    # Constructor
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.initUI()

    def initUI(self):
        self.master.title("Viewer")

        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        canvasW = 800
        canvasH = 450

        canvas = tk.Canvas(self, width=canvasW, height=canvasH)
        rect_color = "#FF00FF"
        canvas.create_rectangle(10, 20, 400, 300, outline=rect_color, fill=rect_color)
        canvas.create_rectangle(1, 1, canvasW, canvasH)
        canvas.pack(fill=tk.BOTH, expand=1)

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

## MAIN
if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
