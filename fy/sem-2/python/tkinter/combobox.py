from msilib.schema import ComboBox
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("F093 / Subhashish Nabajja")

selection = tk.StringVar(value="Hello")

comboBox = ttk.Combobox(root, values=["Hello", "World"], textvariable=selection)
comboBox.pack()



root.mainloop()