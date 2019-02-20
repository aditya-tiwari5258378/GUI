from tkinter import *
import pymysql
import tkinter.messagebox as msg

root = Tk()
#root.state('normal')
root.geometry("600x400+300+100")
root['bg'] = 'yellow'



# def databaseConnection():
#     global conn
#     conn = pymysql.connect("localhost", "root", "", "python")
#     msg.showinfo("Database", "Database connected successfully.")


def ledON():
    conn = pymysql.connect("localhost", "root", "samyak@1997", "python")
    cur = conn.cursor()
    conf = msg.askyesno("Alert!!!", "Are you sure want to led ON ?")
    if (conf):
        cur.execute("UPDATE `iot` SET `status`='ON' WHERE id=100")
        conn.commit()
        bulb=PhotoImage(file="led_on.png")
        l_img.config(image=bulb)
        msg.showinfo("Database", "Database updated successfully.")


def ledOFF():
    conn = pymysql.connect("localhost", "root", "samyak@1997", "python")
    cur = conn.cursor()
    conf = msg.askyesno("Alert!!!", "Are you sure want to led OFF ?")
    if (conf):
        cur.execute("UPDATE `iot` SET `status`='OFF' WHERE id=100")
        conn.commit()
        bulb=PhotoImage(file="led_off.png")
        l_img.config(image=bulb)
        msg.showinfo("Database", "Database updated successfully.")


def fanON():
    conn = pymysql.connect("localhost", "root", "samyak@1997", "python")
    cur = conn.cursor()
    conf = msg.askyesno("Alert!!!", "Are you sure want to fan ON ?")
    if (conf):
        cur.execute("UPDATE `iot` SET `status`='ON' WHERE id=101")
        conn.commit()
        msg.showinfo("Database", "Database updated successfully.")


def fanOFF():
    conn = pymysql.connect("localhost", "root", "samyak@1997", "python")
    cur = conn.cursor()
    conf = msg.askyesno("Alert!!!", "Are you sure want to fan OFF ?")
    if (conf):
        cur.execute("UPDATE `iot` SET `status`='OFF' WHERE id=101")
        conn.commit()
        msg.showinfo("Database", "Database updated successfully.")


conn = pymysql.connect("localhost", "root", "samyak@1997", "python")
cur = conn.cursor()
cur.execute("select status from iot where id=100")
data=cur.fetchone()
if(data[0]=='OFF'):
    bulb=PhotoImage(file="led_off.png")
elif(data[0]=='ON'):
    bulb=PhotoImage(file="led_on.png")
led = Frame(root, width=300, height=200)
led.place(x=200, y=100)
l_img=Label(led,image=bulb,width=120,height=140)
l_img.place(x=160,y=40)
Label(led, text="LED Panel", bg="blue").place(x=50, y=50)
Button(led, text="ON", bg="green", command=ledON).place(x=50, y=100)
Button(led, text="OFF", bg='red', command=ledOFF).place(x=100, y=100)

fan = Frame(root, width=300, height=200)
Label(fan, text="FAN Panel", bg="blue").place(x=100, y=50)
Button(fan, text="ON", bg="green",command=fanON).place(x=100, y=100)
Button(fan, text="OFF", bg='red',command=fanOFF).place(x=150, y=100)
fan.place(x=550, y=100)

root.mainloop()
