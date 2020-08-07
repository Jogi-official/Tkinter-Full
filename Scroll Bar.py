from tkinter import *
root = Tk()
root.geometry("755x455")
root.title("Scrollbar ")
#TODO
# for connecting scroll bar to a widget
#     1: widget(yscroll command = scroll bar.set)
#     2:scrollbar.comfig(command = widget , y view)
scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT , fill = Y)

# listbox = Listbox(root , yscrollcommand  = scrollbar.set)
# for i in range(344):
#     listbox.insert(END,f"Item{i}")

#listbox.pack(fill = "both" , padx = 22 , pady = 45)
text = Text(root , yscrollcommand  = scrollbar.set)
text.pack(fill = BOTH , padx  = 22)
scrollbar.config(command = text.yview)
root.mainloop()