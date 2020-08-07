from tkinter import *

root = Tk()
def akash(event):
    print(f"You clicked on the Button{event.x},{event.y}")
root.title("Events in GUI")
root.geometry("644x334")

widget =Button(root,text ="Click Me Please")
widget.pack()
widget.bind("<Button-1>",akash)
widget.bind("<Double-1>",quit)

root.mainloop()