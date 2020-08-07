from tkinter import *

root = Tk()
def add():
    global i
    lbs.insert(ACTIVE , f"{i}")
    i+=1
i =0
root.geometry("755x455")
root.title("List Box")

lbs = Listbox(root)
lbs.pack()
lbs.insert(END ,"First Item Of List BOX")

Button(root , text = "Add Item" ,command = add).pack()

root.mainloop()