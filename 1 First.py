from tkinter import *

window = Tk()
#width x height
window.geometry("700x700")
# width, height
window.minsize(400,400) #minimum size of the window
#width, size
window.maxsize(900, 900) #maximum size of the window

label =Label(text ="This is GUI")
label.pack()

window.mainloop()