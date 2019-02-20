from tkinter import *
root=Tk()
root.state("normal")
root['bg']="light green"
new_frame=Frame(root,width=300,height=200,bg='violet')
new_frame.place(x=0,y=0)
new_frame1=Frame(root,width=300,height=200,bg='light pink')
new_frame1.place(x=350,y=0)
new_frame2=Frame(root,width=300,height=200,bg='green')
new_frame2.place(x=700,y=0)
new_frame3=Frame(root,width=300,height=200,bg='orange')
new_frame3.place(x=1050,y=0)

#add
num_1=IntVar()
num_2=IntVar()

def add():
    a=num_1.get()
    b=num_2.get()
    l.config(text="Result="+ str(a+b))

Entry(new_frame,textvariable=num_1).place(x=90,y=20)
Entry(new_frame,textvariable=num_2).place(x=90,y=50)
Button(new_frame,text="Add",command=add).place(x=180,y=80)
l=Label(new_frame,text="Result=",bg='light blue')
l.place(x=90,y=110)

#sub

num1=IntVar()
num2=IntVar()

def sub():
    x=num1.get()
    y=num2.get()
    l1.config(text="Result="+str(x-y))

Entry(new_frame1,textvariable=num1).place(x=90,y=20)
Entry(new_frame1,textvariable=num2).place(x=90,y=50)
Button(new_frame1,text="Subtract",command=sub).place(x=180,y=80)
l1=Label(new_frame1,text="Result=",bg='light blue')
l1.place(x=90,y=110)

#multiply

number1=IntVar()
number2=IntVar()

def mult():
    x=number1.get()
    y=number2.get()
    l2.config(text="Result="+str(x*y))

Entry(new_frame2,textvariable=number1).place(x=90,y=20)
Entry(new_frame2,textvariable=number2).place(x=90,y=50)
Button(new_frame2,text="Multiply",command=mult).place(x=180,y=80)
l2=Label(new_frame2,text="Result=",bg='light blue')
l2.place(x=90,y=110)


#division

no1=IntVar()
no2=IntVar()

def div():
    x=no1.get()
    y=no2.get()
    l3.config(text="Result="+str(x/y))

Entry(new_frame3,textvariable=no1).place(x=90,y=20)
Entry(new_frame3,textvariable=no2).place(x=90,y=50)
Button(new_frame3,text="Divide",command=div).place(x=180,y=80)
l3=Label(new_frame3,text="Result=",bg='light blue')
l3.place(x=90,y=110)

root.mainloop()