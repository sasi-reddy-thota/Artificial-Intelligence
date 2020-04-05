import os
import sys
from tkinter import *
from subprocess import call
import os

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
def click_checkinn():
    call(["python", "main1.py"])
def click_list():
    call(["python", "PRODUCT.py"])


class PRODUCT_MANAGEMENT:
    def __init__(self):
        root = Tk()
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  
        _fgcolor = '#000000'  
        _compcolor = '#ffffff'
        _ana1color = '#ffffff' 
        _ana2color = '#ffffff' 
        font14 = "-family {Segoe UI} -size 15 -weight bold -slant "  "roman -underline 0 -overstrike 0"
        font16 = "-family {Swis721 BlkCn BT} -size 40 -weight bold "  "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  "roman -underline 0 -overstrike 0"

        
        root.state("zoomed")
      
        root.title("Product Review Analysis for Genuine Rating")
        root.configure(background="#efccff")
        root.configure(highlightbackground="#99b3ff")
        root.configure(highlightcolor="#99b3ff")



        self.menubar = Menu(root,font=font9,bg=_bgcolor,fg=_fgcolor)
        root.configure(menu = self.menubar)



        self.Frame1 = Frame(root)
        self.Frame1.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#efccff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="#99b3ff")
        self.Frame1.configure(width=925)

        self.Message6 = Message(self.Frame1)
        self.Message6.place(relx=0.09, rely=0.01, relheight=0.30, relwidth=0.86)
        self.Message6.configure(background="#efccff")
        self.Message6.configure(font=font16)
        self.Message6.configure(foreground="black")
        self.Message6.configure(highlightbackground="#d9d9d9")
        self.Message6.configure(highlightcolor="black")
        self.Message6.configure(text='''Welcome to Product Review Analysis for Genuine Rating Systm''')
        self.Message6.configure(width=791)

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.18, rely=0.33, height=103, width=566)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#e7b3ff")
        self.Button2.configure(disabledforeground="#bfbfbf")
        self.Button2.configure(font=font14)
        self.Button2.configure(foreground="black")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''SIGNUP AND LOGIN''')
        self.Button2.configure(width=566)
        self.Button2.configure(command=click_checkinn)


        self.Button5 = Button(self.Frame1)
        self.Button5.place(relx=0.18, rely=0.47, height=103, width=566)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#e7b3ff")
        self.Button5.configure(disabledforeground="#bfbfbf")
        self.Button5.configure(font=font14)
        self.Button5.configure(foreground="black")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''PRODUCT SEARCH''')
        self.Button5.configure(width=566)
        self.Button5.configure(command=click_list)

        self.Button6 = Button(self.Frame1)
        self.Button6.place(relx=0.18, rely=0.61, height=103, width=566)
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#e7b3ff")
        self.Button6.configure(disabledforeground="#bfbfbf")
        self.Button6.configure(font=font14)
        self.Button6.configure(foreground="black")
        self.Button6.configure(highlightbackground="#ffffcc")
        self.Button6.configure(highlightcolor="#ffffcc")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''EXIT''')
        self.Button6.configure(width=566)
        self.Button6.configure(command=quit)
        root.mainloop()


if __name__ == '__main__':
    GUUEST=PRODUCT_MANAGEMENT()


