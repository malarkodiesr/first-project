
from tkinter import ttk

import tkinter as tk
import sqlite3
def connect():
    con1=sqlite3.connect("mk.db")
    cur1=con1.cursor()
    cur1.execute("CREATE TABLE IF NOT EXISTS library5 (Bno INTEGER PRIMARY KEY,Bna TEXT,Auna TEXT,Type TEXT,cost INTEGER,pub TEXT)")
    con1.commit()
    con1.close()
def view():
    con1=sqlite3.connect("mk.db")
    cur1=con1.cursor()
    cur1.execute("SELECT * FROM library5")
    rows=cur1.fetchall()
    for row in rows:
        print(row)
        tree.insert("",tk.END,values=row)
    con1.close()

connect()
root=tk.Tk()
tree=ttk.Treeview(root,column=("Bno","Bna","Auna","Type","cost","pub"),show='headings')
tree.column("#1",anchor=tk.CENTER)
tree.heading("#1",text="Bno")
tree.column("#2",anchor=tk.CENTER)
tree.heading("#2",text="Bna")
tree.column("#3",anchor=tk.CENTER)
tree.heading("#3",text="Auna")
tree.column("#4",anchor=tk.CENTER)
tree.heading("#4",text="Type")
tree.column("#5",anchor=tk.CENTER)
tree.heading("#5",text="cost")
tree.column("#6",anchor=tk.CENTER)
tree.heading("#6",text="pub")
tree.pack()
button=tk.Button(text="display data",command=view)
button.pack(pady=10)
root.mainloop()
