from tkinter import *
from tkinter.ttk import *
root=Tk()
menubar=Menu(root)
file=Menu(menubar,tearoff=0)
menubar.add_cascade(label="about us", menu =file)
menubar.place(x=50,y=50)
file.add_command(label="about us",command=None)
file.place(x=50,y=50)
file.add_separator()
menubar.add_cascade(label ="department",menu=file)
root.config(menu=menubar)
mainloop()
