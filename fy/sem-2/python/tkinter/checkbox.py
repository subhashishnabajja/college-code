import tkinter as tk 
from tkinter import ttk





root = tk.Tk()
root.title("F093 / Subhashish Nabajja")

agreement = tk.StringVar()



def handleAgreement():
    print(agreement.get())

ttk.Checkbutton(
    root,
    text='I agree',
    variable=agreement,
    command=handleAgreement,
    onvalue='agree',
    offvalue='disagree').pack()



root.mainloop()