import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("300x200")
root.title("F093 / Subhashish Nabajja")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)


frame1 = tk.Frame(notebook)
frame1.pack()

frame2 = tk.Frame(notebook)
frame2.pack()

notebook.add(frame1, text="Frame 1")
notebook.add(frame2, text="Frame 2")





root.mainloop()