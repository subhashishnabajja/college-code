import tkinter as tk
from tkinter import ttk

root = tk.Tk()

selected = tk.StringVar()
r1 = ttk.Radiobutton(root, text='Option 1', value='Value 1', variable=selected)
r1.pack()
r2 = ttk.Radiobutton(root, text='Option 2', value='Value 2', variable=selected)
r2.pack()
r3 = ttk.Radiobutton(root, text='Option 3', value='value 3', variable=selected)
r3.pack()


root.mainloop()