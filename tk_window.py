from tkinter import *
from tkinter import ttk

#POA: radio button for FS,FT,L,Z --> may pop up more windows depending on choice
#area to enter function (as str to eval)
#plot button

root = Tk()
root.title("All the transforms")
root.configure(background='#edeff2')
mainframe = ttk.Frame(root,padding="50 50 12 12")

#********* define elements *************
op = StringVar()
FS = ttk.Radiobutton(root,text="Fourier Series",variable=op,value="FS")
FT = ttk.Radiobutton(root,text="Fourier Transform",variable=op,value="FT")
LT = ttk.Radiobutton(root,text="Laplace Transform",variable=op,value="LT")
ZT = ttk.Radiobutton(root,text="Z Transform",variable=op,value="ZT")

label = ttk.Label(root,text="Enter function: ")

fxn = StringVar()
fxnBox = ttk.Entry(root,textvariable=fxn)

plotter = ttk.Button(root,text="Plot")      #add command here

#********* element positions *************
FS.grid(column=1,row=1)
FT.grid(column=2,row=1)
LT.grid(column=3,row=1)
ZT.grid(column=4,row=1)

label.grid(column=1,row=4)

fxnBox.grid(column=2,row=4)

plotter.grid(column=2,row=5)
#***        ***     ***
lastx, lasty = 0, 0

def xy(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y

def addLine(event):
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y))
    lastx, lasty = event.x, event.y

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)

#********* mainloop *************
root.mainloop()
