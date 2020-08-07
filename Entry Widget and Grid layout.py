from tkinter import *

def getvalue():
    print(uservalue.get())
    print(passvalue.get())

root =Tk()
root.geometry("655x333")

user = Label(root , text = "Username")
password = Label(root , text = "Password")

user.grid()
password.grid(row = 1)

# Variable Classes in TKINter
#
# BooleanVar
# DoubleVar
# StringVar
# IntVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root , textvariable = uservalue)
passentry = Entry(root , textvariable = passvalue)

userentry.grid(row = 0 , column = 1)
passentry.grid(row = 1 , column = 1)

Button(text ="Sumbit" , command = getvalue).grid(row  = 3 , column = 2)
root.mainloop()