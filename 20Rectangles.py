#Display Rectangles
#Python 3.7.2
#Eric Zhang
#0940485
#April  8, 2019
#PC, Windows 10

from tkinter import *

class Panel:
    def __init__(self):
        window = Tk()
        window.title("Display Rectangles")

        self.canvas = Canvas(window, width=350, height = 200, bg = "white")
        self.canvas.pack()
        
        frame = Frame(window)
        frame.pack()

        self.canvas.delete(ALL)

        x1,y1,x2,y2 = 100,99,250,101
        for i in range(20):           
            self.canvas.create_rectangle(x1,y1,x2,y2)
            x1-=5
            y1-=5
            x2+=5
            y2+=5
        window.mainloop()
Panel()



