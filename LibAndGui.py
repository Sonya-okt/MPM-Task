# Importing everything from tkinter
from tkinter import *
from tkinter.messagebox import showerror

# Creating a GUI
root = Tk()
root.title("PythonGeeks Calculator")
root.geometry('265x500')
root.resizable(0, 0)
root.configure(background='LightCyan2')
# StringVar variables
entry_strvar = StringVar(root)
# Defining the top
Label(root, text='KalkulaTHOR', font=("Comic Sans MS", 15), bg='white').place(x=25, y=0)
Label(root, text='Press \'x\' twice for exponentiation', font=("Georgia", 10), bg='blue').place(x=30, y=30)
eqn_entry = Entry(root, justify=RIGHT, textvariable=entry_strvar, width=22, font=12, state='disabled')
eqn_entry.place(x=10, y=70)
# Updating root
root.update()
root.mainloop()
