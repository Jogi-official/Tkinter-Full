from tkinter import *

root = Tk()
root.geometry("644x566")
import tkinter.messagebox as tmsg
#var = IntVar()
var = StringVar()
var.set("RADIO")
#var.set(1)
def order():
    tmsg.showinfo("Order Recieved",f"You have selected {var.get()}")

Label(root , text = "What would to like to have sir ?",font = "lucida 19 bold", justify = LEFT  , padx = 14 ).pack()
radio = Radiobutton(root , text = "DOSA" , padx = 14 , variable = var , value = "DOSA").pack(anchor = "w")
radio = Radiobutton(root , text = "IDLI" , padx = 14 , variable = var , value = "IDLI").pack(anchor = "w")
radio = Radiobutton(root , text = "PARATHA" , padx = 14 , variable = var , value = "PARATHA").pack(anchor = "w")
radio = Radiobutton(root , text = "SAMOSA" , padx = 14 , variable = var , value = "SAMOSA").pack(anchor = "w")


Button(text = "Order Now ",command = order).pack()


root.mainloop()