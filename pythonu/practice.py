import mysql.connector

con=mysql.connector.connect(
    host="hostname",
    user="username",
    password="password",
    database="database"
)

cur=con.cursor()


cur.execute("SELECT IMAGE FROM PICTURE WHERE PIN=1")
data=cur.fetchall()[0]
f=open("image","wb")
f.write(data)
f.close()
con.commit()
con.close()
