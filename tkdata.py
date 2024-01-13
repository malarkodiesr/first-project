import sqlite3
conn=sqlite3.connect('mk.db')
cursor=conn.cursor()
table="create table library5(Bno int,Bna char(50),Auna char(50),Type char(50),cost int,pub char(60));"
cursor.execute(table)
cursor.execute("insert into library5(Bno,Bna,Auna,Type,cost,pub)values(12,'think positive','bruce','recieved',300,'maya')")
cursor.execute("insert into library5(Bno,Bna,Auna,Type,cost,pub)values(13,'universe','andrew','lended',400,'select pub')")
cursor.execute("insert into library5(Bno,Bna,Auna,Type,cost,pub)values(14,'Thayam','mahatria','lended',350,'maya pub')")
print("data inserted in the table")
data=cursor.execute("select* from library5")
for row in data:
    print(row)
conn.commit()
conn.close()
