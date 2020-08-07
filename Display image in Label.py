from tkinter import *
#pip install pillow
#Tkinter doesnt support jpg yet so for using the jpg images we will use the Pilow lib

from PIL import Image, ImageTk
window = Tk()

window.geometry("1255x944")
#photo =PhotoImage(file ="insta.png")

#for jpg images

image = Image.open("insta.jpg")
photo = ImageTk.PhotoImage(image)

label = Label(image = photo)
label.pack()
window.mainloop()