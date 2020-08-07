from tkinter import *

#self here is my Tk()
#super class is called because when we were not creatimng the class the TK import all the funcations but now we have to nesure that it calls everything
class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("655x455")
    def status (self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self ,textvar = self.var , relief = SUNKEN , anchor ="w")
        self.statusbar.pack(side = BOTTOM , fill = X )

    def click(self):
        print("Button clicked")

    def createButton(self , inptext):
        Button(text = inptext , command = self.click).pack()
if __name__ == '__main__':
    window = GUI()
    window.createButton("Click ME")
    window.status()
    window.mainloop()