#Display Cicles
#Python 3.7.2
#Eric Zhang
#0940485
#April  14, 2019
#PC, Windows 10

from tkinter import *

class Circles:
    def __init__(self):
        window = Tk()
        window.title("Dynamic Circles")

        self.canvas = Canvas(window, width=200, height = 200, bg = "white")
        self.canvas.pack()
        
        frame = Frame(window)
        frame.pack()

        self.x1, self.y1, self.x2, self.y2 = 90,90,110,110
        
        self.canvas.delete(ALL)

        self.canvas.bind("<Button-1>", self.addCircle)
        self.canvas.bind("<Button-3>", self.deleteCircle)

        self.myCircles = []
                
        window.mainloop()

    def addCircle(self, event):
        self.x1-=5
        self.y1-=5
        self.x2+=5
        self.y2+=5
        self.newCircle = self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2)
        self.myCircles.append(self.newCircle)
    def deleteCircle(self, event):
        if len(self.myCircles) == 0:
            print("No more circles left")
        else:       
            self.x1+=5
            self.y1+=5
            self.x2-=5
            self.y2-=5
            A = self.myCircles.pop()
            self.canvas.delete(A)

Circles()

