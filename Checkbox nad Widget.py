from tkinter import *

root = Tk()

def getvalue():
    print("Sumbitting Form")
    print(f"{namevalue.get(),phonevalue.get() ,gendervalue.get(),emergencyvalue.get(),paymentvalue.get(),foodservice.get()}")
    with open("records.txt","a" ) as f:
        f.write(f"{namevalue.get(),phonevalue.get() ,gendervalue.get(),emergencyvalue.get(),paymentvalue.get(),foodservice.get()}\n")


root.geometry("644x344")
Label(root , text = "Welcome to Akash Travels" , font ="comicsansas 12 bold" , padx = 22).grid(row = 0 , column  = 3)
name = Label(root , text ="Name" )
phone = Label(root , text ="Phone" )
gender = Label(root , text ="Gender" )
emergency = Label(root , text ="Emergency Number" )
payment = Label(root , text ="Payement mode" )

name.grid(row = 1 ,column = 2)
phone.grid(row = 2,column = 2)
gender.grid(row = 3 ,column = 2)
emergency.grid(row = 4,column = 2)
payment.grid(row = 5,column = 2)

namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentvalue = StringVar()

foodservice = IntVar()



nameentry = Entry(root , textvariable =namevalue )
phoneentry = Entry(root , textvariable =phonevalue )
genderentry = Entry(root , textvariable =gendervalue )
emergencyentry = Entry(root , textvariable = emergencyvalue)
paymententry = Entry(root , textvariable = paymentvalue)

nameentry.grid(row = 1 , column = 3)
phoneentry.grid(row = 2 , column = 3)
genderentry.grid(row = 3 , column = 3)
emergencyentry.grid(row = 4 , column = 3)
paymententry.grid(row = 5 , column = 3)

foodserviceVariable  = Checkbutton(text = "Want to prebook your meals" , variable = foodservice , pady = 12 , padx = 12)
foodserviceVariable.grid(row = 6 , column = 3)

Button(text ="Sumbit" , command = getvalue).grid( row = 7 , column = 3 )

root.mainloop()