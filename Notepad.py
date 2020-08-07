from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename ,asksaveasfilename
import os
def newFile():
    global file
    root.title("Untitled -NOtepad")
    file =None
    TextArea.delete(1.0 , END)

def openFile():
    global file
    file = askopenfilename(defaultextension = ".txt" , filetypes =[("All Files","*.*"),("Text Documnets","*.txt")])
    if file == " ":
        file =None
    else:
        root.title(os.path.basename(file) + "-Notepad")
        TextArea.delete(1.0,END)
        f =open(file, "r")
        TextArea.insert(1.0 ,f.read())
        f.close()
def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            # Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()



def quitApp():
    root.destroy()
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    tmsg.showinfo("NOTEPAD","Enjoy!!! REGARDS FROM TEAM JOGI")


if __name__ == '__main__':
    #basic tkinter setup
    root = Tk()
    root.title("Notepad")
    root.wm_iconbitmap("apple.ico")

    #Add text area
    TextArea = Text(root , font = "luicida 13")
    file = None
    TextArea.pack(expand = True , fill =BOTH)

    #Menu BAR
    MenuBar = Menu(root)

    #File menu start
    Filemenu = Menu(MenuBar , tearoff = 0 )
    #to open new file
    Filemenu.add_command(label ="New" , command = newFile)

    #To open Aleready existing file
    Filemenu.add_command(label = "Open" , command = openFile)

    #to save the curren t file

    Filemenu.add_command(label ="Save" , command =saveFile)
    Filemenu.add_separator()

    #add exit command

    Filemenu.add_command(label = "Exit" , command = quitApp)

    MenuBar.add_cascade(label = "File" , menu =Filemenu)


    #Edit MEnu Starts

    Editmenu = Menu(MenuBar , tearoff =0 )
    Editmenu.add_command(label = "Cut" , command = cut )
    Editmenu.add_command(label = "Copy" , command = copy )
    Editmenu.add_command(label = "Paste" , command = paste )
    MenuBar.add_cascade(label = "Edit" , menu = Editmenu)

    #help Menu
    helpmenu = Menu(MenuBar , tearoff = 0)
    helpmenu.add_command(label ="About Notepad",command = about)
    MenuBar.add_cascade(label ="Help" , menu = helpmenu)

    root.config(menu=MenuBar)

    #adding scroll bar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side = RIGHT , fill = Y)
    Scroll.config(command = TextArea.yview)
    TextArea.config(yscrollcommand = Scroll.set)

    root.mainloop()




