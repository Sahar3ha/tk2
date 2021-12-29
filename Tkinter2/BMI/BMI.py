#BMI
from tkinter import *

root=Tk()

root.geometry("600x400")
a=Label(root, text="Enter a mass :")
a.place(x=30,y=50)
e1=Entry(root)
e1.place(x=140,y=50)
b=Label(root, text="Enter a height :")
b.place(x=30,y=90)
e2=Entry(root)
e2.place(x=140,y=90)

def click():
    c=int(e1.get())
    d=int(e2.get())
    bmi=(c/d*d)
    l1=Label(root, text=("The BMI is:",bmi))
    l1.place(x=240,y=290)

b1=Button(root, text="Calculate", command=click)
b1.place(x=240,y=250)

root.mainloop()

