from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
def myfunc():
    print("Akash Joshi")

def help():
    print("I will Help You")
    a =tmsg.showinfo("Help","I will help you ")
def rate():
    print("Rate us ")
    value = tmsg.askquestion("was your experience Good" , "you used thi GUI was this good ?")
    if value == "yes":
        msg = "Great Rate us on App store "
    else:
        msg ="We will solve this soon "
    tmsg.showinfo("Experience",msg)
def divya():
    ans =tmsg.askretrycancel("Divya yes " , "Divya no ")
    if ans:
        msg = "Retry krne pe kuch nhi hoga"
    else:
        msg = "Cancel krdiya warna pit ta"
    tmsg.showinfo("NOTE",msg)

root.geometry("733x566")
root.title("Menu and Submenus")

mainmenu  = Menu(root)
m1 =Menu(mainmenu  , tearoff = 0)
m1.add_command(label ="New Project" , command = myfunc)
m1.add_command(label ="Save" , command = myfunc)
m1.add_separator()
m1.add_command(label ="Save As" , command = myfunc)
m1.add_command(label ="Print" , command = myfunc)
root.config(menu = mainmenu )
mainmenu .add_cascade(label="File", menu = m1)

m2  =Menu(mainmenu  , tearoff = 0)
m2 .add_command(label ="Cut" , command = myfunc)
m2 .add_command(label ="Copy" , command = myfunc)
m2 .add_separator()
m2 .add_command(label ="Paste" , command = myfunc)
m2 .add_command(label ="Run" , command = myfunc)
root.config(menu = mainmenu )
mainmenu .add_cascade(label="Edit", menu = m2 )

m3  =Menu(mainmenu  , tearoff = 0)
m3 .add_command(label ="Help" , command = help)
m3 .add_command(label ="Rate US" , command = rate)
m3 .add_command(label ="Befriend Divya" , command = divya)
mainmenu.add_cascade(label ="Help" ,menu = m3)
root.config(menu = mainmenu)



root.mainloop()