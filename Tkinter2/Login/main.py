from tkinter import *

root = Tk()
root.geometry("400x200")

a=Label(root, text="Username").place(x=30,y=50)
e1=Entry(root).place(x=100,y=50)
b=Label(root, text="Password").place(x=30,y=90)
e2=Entry(root).place(x=100,y=90)
c=Button(root, text="Login").place(x=150,y=120)
d=Button(root, text="Cancel").place(x=200,y=120)

root.mainloop()