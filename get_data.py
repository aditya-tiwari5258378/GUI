import pymysql
import time
while(True):
    conn=pymysql.connect("localhost","root","pass","python")
    cur=conn.cursor()
    cur.execute("select status from iot where id=100")
    data=cur.fetchone()
    print(data[0])
    time.sleep(0.5)
