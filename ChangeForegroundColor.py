#Change foreground colors
#Python 3.7.2
#Eric Zhang
#0940485
#14 April 2019
#PC Windows 10

from tkinter import *

class ForegroundColor:
    def __init__(self):
        window = Tk()
        window.title("Set Colors")
        window.geometry('200x100')

        color = StringVar()
        #color options: red, green, blue, yellow, purple, orange
        color.set("red")
        colorSelect = OptionMenu(window, color, "red", "green", \
                             "blue", "yellow", "purple", "orange",\
                             command = self.changeColor)
        colorSelect.pack()

        
        self.text = Label(window, text = "Programming is fun", fg = "red")
        self.text.pack()

        window.mainloop()

    def changeColor(self, selectedColor):
        if selectedColor == "red":
            self.text.config(fg = "red")
        if selectedColor == "green":
            self.text.config(fg = "green")
        if selectedColor == "blue":
            self.text.config(fg = "blue")
        if selectedColor == "yellow":
            self.text.config(fg = "yellow")
        if selectedColor == "purple":
            self.text.config(fg = "purple")
        if selectedColor == "orange":
            self.text.config(fg = "orange")


ForegroundColor()
