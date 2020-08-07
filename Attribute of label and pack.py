from tkinter import *

window = Tk()
window.geometry("744x433")
window.title("GUI Program")

#IMportant Label Options
# text---Adds the text
# bd ---background
# font--- sets the font
# padx-- xpadding
# pady --y padding
# relief---border styling ---SUNKEN , ,GROOVE ,RIDGE
title_label =Label(text = '''ANY was an architectural journal,[1] published by the ANYone Corporation for over seven years. A total of 27 issues \nwere published. The first issue was published in May 1993, and its last was published in September 2000.[2][3] ANY was succeeded by Log, also \npublished by the ANYone Corporation.Notable contributors to the magazine included Zaha Hadid, Bernard Tschumi, Elizabeth Diller, Rem Koolhaas,\n[4] Sanford Kwinter, R.E. Somol, Peter Eisenman, and Greg Lynn.[5]Issues one to eight were designed by longtime Eisenman collaborator, Massimo \nVignelli. Beginning with number eight, the magazine was designed by graphic design firm, 2x4.[1]''', bg = "red" , fg = "white" , padx =13 , pady  = 94 , font =("comicsansms",9 ,"bold"),borderwidth = 3, relief =SUNKEN)
# Important Pack options
# anchor = N , W , E ,NW , NE , S
#side = top , bottom , left , right
#fill
#padx
#pady


#title_label.pack(side =BOTTOM ,anchor = "sw" ,fill = X)
title_label.pack(side =LEFT,fill = Y , padx = 34 , pady = 34)
window.mainloop()