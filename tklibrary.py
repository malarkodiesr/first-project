from tkinter import*
import sqlite3
import tkinter as tk
import tkinter.messagebox as m

master=Tk()
group=LabelFrame(master,text="Library Data Entry screen",padx=15,pady=15)
group.pack(padx=15,pady=15)
conn=sqlite3.connect('mk.db')
cursor=conn.cursor()
conn.execute("SELECT * FROM LIBRARY5")

T1=IntVar()
T2=StringVar()
T3=StringVar()
T4= IntVar()
T5=StringVar()
c1=StringVar()
Btype=StringVar()
def clear():
    T1.set(0)
    T2.set(" ")
    T3.set(" ")
    T4.set(0)
    T5.set(" ")

    
def show():
    sql="select * from library5"
    data=cursor.execute(sql)
    for row in data:
        print(row)
        conn.commit()
def search():
    sql2="select * from library where bno="+str(T1.get())
    data1=cursor.execute(sql2)
    
    for row in data1:
        T2.set(row[1])
        T3.set(row[2])
        T4.set(row[3])
        T5.set(row[4])
    conn.commit()
def delete():
    sql="delete from library5"
    cursor.execute(sql)
    conn.commit()
    m.showinfo("TABLE","ALL DATAS ERASED IN TABLE")
def close():
    master.destroy()
def add():
    if c1.get()=="R":
        Btype="Recieved"
    else:
        Btype="Lended"
    sql="insert into Library5(bno,bna,auna,type,cost,pub) values (%d,'%s','%s','%s',%d,'%s')"%(int(T1.get()),T2.get(),Btype,T3.get(),(int(T4.get())),T5.get())
    #sql1="insert into Library(bno) values ('%d')"%(T1.get())
    #print(sql)
    m.showinfo("TABLE","ONE DATA INSERTED IN TABLE")
    cursor.execute(sql)
    conn.commit()
Label(group,text="Book no").grid(row=0,column=3)
w=Entry(group,textvariable=T1).grid(row=0,column=20)
Label(group,text="Book name").grid(row=2,column=3)
w1=Entry(group,textvariable=T2).grid(row=2,column=20)
Label(group,text="Author name").grid(row=6,column=3)
w3=Entry(group,textvariable=T3).grid(row=6,column=20)
Label(group,text="Type").grid(row=4,column=3)
R1=Radiobutton(group,text="Recieved",variable=c1,value="R").grid(row=4,column=20)
R2=Radiobutton(group,text="Lended",variable=c1,value="L").grid(row=4,column=25)
b1=Button(group,text="ADD",command=add).grid(row=7,column=25)
w4=Entry(group,textvariable=T4).grid(row=8,column=20)
Label(group,text="cost").grid(row=8,column=3)
w5=Entry(group,textvariable=T5).grid(row=9,column=20)
Label(group,text="Publication").grid(row=9,column=3)
b2=Button(group,text="delete",command=delete).grid(row=10,column=3)
b3=Button(group,text="clear",command=clear).grid(row=10,column=15)
b4=Button(group,text="search",command=search).grid(row=10,column=20)
b5=Button(group,text="show",command=show).grid(row=10,column=25)
b6=Button(group,text="close",command=close).grid(row=10,column=30)
#b7=Button(group,text="grid",command=
c1.set("R")
mainloop()
conn.close()



