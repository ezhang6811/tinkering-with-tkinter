#Select Geometric Figures
#Python 3.7.2
#Eric Zhang
#0940485
#April  7, 2019
#PC, Windows 10

from tkinter import *

class Panel:
    def __init__(self):
        window = Tk()
        window.title("Radiobuttons and Checkbuttons")

        self.canvas = Canvas(window, width=200, height = 100, bg = "white")
        self.canvas.pack()
        
        frame = Frame(window)
        frame.pack()

        self.x = IntVar()
        self.y = IntVar()

        rbRectangle = Radiobutton(frame, text = "Rectangle", variable = self.x, \
                                  value = 1, command = self.drawRectangle)
        rbOval = Radiobutton(frame, text = "Oval", variable = self.x, \
                             value = 2, command = self.drawOval)
        cbFill = Checkbutton(frame, text = "Filled", variable = self.y, \
                             command = self.fillShape)


        rbRectangle.grid(row = 1, column = 1)
        rbOval.grid(row = 1, column = 2)
        cbFill.grid(row = 1, column = 3)

        window.mainloop()

    def clearCanvas(self):
        self.canvas.delete(ALL)
    def drawRectangle(self):
        self.clearCanvas()
        self.canvas.create_rectangle(10, 10, 190, 90)
    def drawOval(self):
        self.clearCanvas()
        self.canvas.create_oval(10, 10, 190, 90)
    def fillShape(self):
        if self.x.get() == 1:
            if self.y.get() == 1:
                self.clearCanvas()
                self.canvas.create_rectangle(10, 10, 190, 90, fill = "red")
            else:
                self.clearCanvas()
                self.canvas.create_rectangle(10, 10, 190, 90)
        if self.x.get() == 2:
            if self.y.get() == 1:
                self.clearCanvas()
                self.canvas.create_oval(10, 10, 190, 90, fill = "red")
            else:
                self.clearCanvas()
                self.canvas.create_oval(10, 10, 190, 90)
                

Panel()



