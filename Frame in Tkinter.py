from tkinter import *

window = Tk()
window.geometry("655x333")
f1 =Frame(window, bg ="grey" ,borderwidth = 6 ,relief =SUNKEN)
f1.pack(side = LEFT , fill ="y")

f2 = Frame(window, borderwidth = 8 , bg = "grey" , relief = SUNKEN)
f2.pack(side = TOP , fill = "x")

l1 =Label(f1 , text ="PROJECT Tkinter ---PYCharm")
l1.pack(pady = 142)
l =Label(f2 , text ="Welcome Akash Joshi ",font ="Helvetica 16 bold",fg ="red",pady = 4)
l.pack()
window.mainloop()