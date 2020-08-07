from tkinter import *

root = Tk()
root.geometry("644x455")
root.title("Title of GUI ")

#.icu type of file for the application image
root.wm_iconbitmap("apple.ico")
root.config(background = "gray")

width = root.winfo_screenmmwidth()
height = root.winfo_screenheight()

print(f"{width}x{height}")
Button(text = "Close" , command = root.destroy).pack()


root.mainloop()