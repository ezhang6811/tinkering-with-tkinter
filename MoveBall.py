#Move the Ball
#Python 3.7.2
#Eric Zhang
#0940485
#April  7, 2019
#PC, Windows 10

from tkinter import *

class Panel:
    def __init__(self, x1 = 395, y1 = 195, x2 = 405, y2 = 205):
        window = Tk()
        window.title("Moving Ball")

        self.canvas = Canvas(window, width=800, height = 400, bg = "white")
        self.canvas.pack()

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.canvas.create_oval(x1, y1, x2, y2)
        
        frame = Frame(window)
        frame.pack()
        btLeft = Button(frame, text = "Left", command = self.goLeft)
        btRight = Button(frame, text = "Right", command = self.goRight)
        btUp = Button(frame, text = "Up", command = self.goUp)
        btDown = Button(frame, text = "Down", command = self.goDown)

        btLeft.grid(row = 1, column = 1)
        btRight.grid(row = 1, column = 2)
        btUp.grid(row = 1, column = 3)
        btDown.grid(row = 1, column = 4)

        window.mainloop()

    def clearCanvas(self):
        self.canvas.delete(ALL)
    def goLeft(self):
        if self.x1 > 5:
            self.x1-=10
            self.x2-=10
        self.clearCanvas()
        self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill = "red")
    def goRight(self):
        if self.x2 < 795:
            self.x1+=10
            self.x2+=10
        self.clearCanvas()
        self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill = "red")
    def goUp(self):
        if self.y1 > 5:
            self.y1-=10
            self.y2-=10
        self.clearCanvas()
        self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill = "red")
    def goDown(self):
        if self.y2 < 395:
            self.y1+=10
            self.y2+=10
        self.clearCanvas()
        self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill = "red")

Panel()



