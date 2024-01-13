from tkinter import *
import tkinter as ak



import sys
import os
master=ak.Tk()


def openfile():
    import tklibrary as tk1
    
def openfile2():
    import tkgrid1 as tk2
    
    
    

button1=Button(master,text="Run main file",font=('bold',15),fg='#158aff',bd=0,bg='#c3c3c3',command=openfile)
#button1.place(x=10,y=50)

button2=Button(master,text="Run grid view",font=('bold',15),fg='#158aff',bd=0,bg='#c3c3c3',command=openfile2)
#button2.place(x=10,y=150)

button1.pack(pady=50)

button2.pack(pady=100)

mainloop()
