from tkinter import *
root =Tk()
def click(event):
    global scvalue
    text = event.widget.cget("text")  #widget se text nikalne ke liye use hota hai
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+ text )
        screen.update()

root.geometry("644x900")
root.title("Calculator")

scvalue = StringVar()
scvalue.set("")
screen =Entry(root , textvar =scvalue , font = "luicida 40 bold")
screen.pack(fill = X , ipadx = 1 , pady = 10 , padx = 10 )

root.wm_iconbitmap("apple.ico")


f = Frame(root ,bg ="red")
b = Button(f , text ="9" , font = "luicida 31 bold" ,padx = 11 , pady = 1 )
b.pack(padx = 1 , pady = 11 ,side = LEFT)
b.bind("<Button-1>",click)

b = Button(f , text ="1" , font = "luicida 31 bold" ,padx = 11 , pady = 1 )
b.pack(padx = 1 , pady = 11 , side = LEFT)
b.bind("<Button-1>",click)

b = Button(f , text ="7" , font = "luicida 31 bold" ,padx = 11 , pady = 1 )
b.pack(padx = 1 , pady = 11 , side = LEFT)
b.bind("<Button-1>",click)

f.pack()





f = Frame(root , bg = "red")
b = Button(f , text ="6" , font = "luicida 31 bold" ,padx = 11 , pady = 1 )
b.pack(padx = 1 , pady = 11 ,side = LEFT ,fill = X)
b.bind("<Button-1>",click)

b = Button(f , text ="1" , font = "luicida 31 bold" ,padx = 11 , pady = 1 )
b.pack(padx = 1 , pady = 11 , side = LEFT)
b.bind("<Button-1>",click)

b = Button(f , text ="4" , font = "luicida 31 bold" ,padx = 11 , pady = 1 )
b.pack(padx = 1 , pady = 11 , side = LEFT)
b.bind("<Button-1>",click)

f.pack()


f = Frame(root , bg = "red")
b = Button(f , text ="3" , font = "luicida 31 bold" ,padx = 11 , pady = 1 )
b.pack(padx = 1 , pady = 11 ,side = LEFT)
b.bind("<Button-1>",click)

b = Button(f , text ="2" , font = "luicida 31 bold" ,padx = 11 , pady = 1 )
b.pack(padx = 1 , pady = 11 , side = LEFT)
b.bind("<Button-1>",click)

b = Button(f , text ="1" , font = "luicida 31 bold" ,padx = 11 , pady = 1 )
b.pack(padx = 1 , pady = 11 , side = LEFT)
b.bind("<Button-1>",click)

f.pack()


f = Frame(root , bg = "red")
b = Button(f , text ="0" , font = "luicida 31 bold" ,padx = 12.5 , pady = 1 )
b.pack(padx = 1 , pady = 11 ,side = LEFT)
b.bind("<Button-1>",click)

b = Button(f , text ="+" , font = "luicida 31 bold" ,padx = 12 , pady = 1 )
b.pack(padx = 1 , pady = 11 , side = LEFT)
b.bind("<Button-1>",click)

b = Button(f , text ="-" , font = "luicida 31 bold" ,padx = 12 , pady = 1 )
b.pack(padx = 1 , pady = 11 , side = LEFT)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root , bg = "red")
b = Button(f , text ="/" , font = "luicida 31 bold" ,padx = 12.5 , pady = 1 )
b.pack(padx = 1 , pady = 11 ,side = LEFT)
b.bind("<Button-1>",click)

b = Button(f , text ="*" , font = "luicida 31 bold" ,padx = 12 , pady = 1 )
b.pack(padx = 1 , pady = 11 , side = LEFT)
b.bind("<Button-1>",click)

b = Button(f , text ="%" , font = "luicida 31 bold" ,padx = 12 , pady = 1 )
b.pack(padx = 1 , pady = 11 , side = LEFT)
b.bind("<Button-1>",click)

f.pack()


f = Frame(root , bg = "red")
b = Button(f , text ="C" , font = "luicida 31 bold" ,padx = 20 , pady = 1 )
b.pack(padx = 2 , pady = 11 ,side = LEFT)
b.bind("<Button-1>",click)

b = Button(f , text ="=" , font = "luicida 31 bold" ,padx = 20, pady = 1 )
b.pack(padx = 19 , pady = 5 , side = LEFT)
b.bind("<Button-1>",click)

f.pack()



root.mainloop()