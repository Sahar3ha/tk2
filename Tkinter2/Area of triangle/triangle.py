#area of triangle
from tkinter import *

#declaration of root
root=Tk()
root.geometry("600x400")

#creation of entry 1
a=Label(root, text="Base :").pack()
e1=Entry(root)
e1.pack()
b=Label(root, text="Height :").pack()
e2=Entry(root)
e2.pack()


def click():
    ac=int(e1.get())
    bc=int(e2.get())
    ec=(ac*bc)/2

    l1=Label(root, text=("The area of traiangle is:",ec))
    l1.pack()

b1=Button(root, text="Calculate", command=click)
b1.pack()



root.mainloop()    