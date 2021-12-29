#volume of cuboid

from tkinter import *

#declaration of root
root = Tk()
root.geometry("600x400")

#creation of entry 1
a=Label(root, text="Length :").pack()
e1=Entry(root)
e1.pack()


def click():
    ac=int(e1.get())
    ec=(ac*ac*ac)

    l1=Label(root, text=("The volume of cube is:",ec))
    l1.pack()

b1=Button(root, text="Calculate", command=click)
b1.pack()



root.mainloop()    