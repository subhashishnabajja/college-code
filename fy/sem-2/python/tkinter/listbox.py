import tkinter as tk
from tkinter import ttk 


root = tk.Tk()
root.title("F093 / Subhashish Nabajja")
root.geometry("300x200")

def handleSelect(event):
    print(listbox.get(listbox.curselection()))

langs = ('Java', 'C#', 'C', 'C++', 'Python',
        'Go', 'JavaScript', 'PHP', 'Swift')

listVariable = tk.StringVar(value=langs)

listbox = tk.Listbox(root, listvariable=listVariable, selectmode="extended" )
listbox.pack()
listbox.bind('<<ListboxSelect>>', handleSelect)

root.mainloop()