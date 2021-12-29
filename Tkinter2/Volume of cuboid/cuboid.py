#volume of cuboid

from tkinter import *

#declaration of root
root = Tk()
root.geometry("600x400")

#creation of entry 1
a=Label(root, text="Length :").pack()
e1=Entry(root)
e1.pack()
b=Label(root, text="Breadth :").pack()
e2=Entry(root)
e2.pack()
c=Label(root, text="Width :").pack()
e3=Entry(root)
e3.pack()


def click():
    ac=int(e1.get())
    bc=int(e2.get())
    cc=int(e3.get())
    ec=(ac*bc*cc)

    l1=Label(root, text=("The volume of cuboid is:",ec))
    l1.pack()

b1=Button(root, text="Calculate", command=click)
b1.pack()



root.mainloop()    