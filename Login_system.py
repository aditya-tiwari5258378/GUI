from tkinter import *
import pymysql
import tkinter.messagebox as tm

root=Tk()
root.state("normal")
root['bg']="light green"
new_frame=Frame(root,width=300,height=400,bg='violet')
new_frame.place(x=500,y=200)


user_id = IntVar()
user_name = StringVar()
user_address = StringVar()
user_phone = IntVar()
file=open("hello.txt","w")


def Login():
    conn=pymysql.connect("localhost","root","naruto378","check_py")
    cur=conn.cursor()
    user_id1=user_id.get()
    user_name1=user_name.get()
    user_address1=user_address.get()
    user_phone1=user_phone.get()


    in_sql="insert into user_in values("+ str(user_id1) + ",'" + user_name1+"','"+ user_address1+"'," + str(user_phone1)+")"
    cur.execute(in_sql)
    conn.commit()
    print("Hello Python",file=file)
    file.close()
    tm.showinfo("Messsage","Data inserted successfully.")


    new_win=Toplevel()
    Button(new_win,text="Thank u",command=new_win.destroy).pack()
    new_win.mainloop()

b=Button(root,text="Login",bg='light green',borderwidth=10,
           fg='black',font=("arial",10,"bold"),command=Login)
b.place(x=550,y=380)
#entering fields
Entry(new_frame,textvariable=user_id).place(x=90, y=20)
Entry(new_frame, textvariable=user_name).place(x=110, y=50)
Entry(new_frame, textvariable=user_address).place(x=90, y=80)
Entry(new_frame, textvariable=user_phone).place(x=80, y=110)
Label(new_frame,text="User Id",bg='light blue',fg='black').place(x=30,y=20)
Label(new_frame,text="User Name",bg='light blue',fg='black').place(x=30,y=50)
Label(new_frame,text="Address",bg='light blue',fg='black').place(x=30,y=80)
Label(new_frame,text="Phone",bg='light blue',fg='black').place(x=30,y=110)

root.mainloop()