from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("744x456")
root.title("Sliders")

def getdollar():
    print(f"Money Credited{myslider2.get()} in your bank account")
    tmsg.showinfo("Amount Credited",f"Money Credited{myslider2.get()} in your bank account")
# myslider = Scale(root , from_ = 0 , to = 100 )
# myslider.pack()
Label(root , text = "How many dollars do you want ?").pack()
myslider2 = Scale(root , from_ = 0 , to = 100 ,orient = HORIZONTAL , tickinterval = 50 )
#myslider2.set(34) # for default values
myslider2.pack()
Button(root , text = "Get Dollars" ,pady = 10 , command = getdollar).pack()



root.mainloop()