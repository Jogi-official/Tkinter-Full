from tkinter import *
root = Tk()
root.geometry('655x333')

def hello():
    print("helllooooooooooo")


frame = Frame(root , borderwidth = 6 , bg = "grey" , relief = SUNKEN)
frame.pack(side = LEFT , anchor ="ne")

b1 = Button(frame ,fg = "red",text="Print Now",command = hello)
b1.pack(side = LEFT  ,padx = 23 )

b2 = Button(frame ,fg = "red",text="Print Now")
b2.pack(side = LEFT  ,padx = 23)

b3 = Button(frame ,fg = "red",text="Print Now")
b3.pack(side = LEFT  ,padx = 23)

b4 = Button(frame ,fg = "red",text="Print Now")
b4.pack(side = LEFT  ,padx = 23)

root.mainloop()