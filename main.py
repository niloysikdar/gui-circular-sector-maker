#Author : Niloy Sikdar

from tkinter import *

win = Tk()
win.title("Arc with sliders")
win.geometry("850x750")

def createArc(var):
    canvas.delete("all")
    canvas.create_arc(0,0,800,600, start = slider1.get(), extent = slider2.get(), fill="blue")

label1 = Label(win, text="Start")
label1.pack()
slider1 = Scale(win, from_=0 , to=360, orient=HORIZONTAL, length=600, command = createArc)
slider1.pack()
label2 = Label(win, text="End")
label2.pack()
slider2 = Scale(win, from_=0 , to=360, orient=HORIZONTAL, length=600, command = createArc)
slider2.pack()

canvas = Canvas(win, height=600, width=800, bg = "pink")
canvas.pack()

win.mainloop()