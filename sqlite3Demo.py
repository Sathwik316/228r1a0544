import sqlite3
con=sqlite3.connect("mydatabase.db")
cur=con.cursor()
#cur.execute("create table students(name varchar(50),roll_no varchar(50),password varchar(50))")
#cur.execute('insert into students values("raju","101","A")')
#cur.execute('insert into students values("ramesh","102","B")')
#cur.execute('insert into students values("ravi","103","C")')
cur.execute('delete from students where name="raju" ')
cur.execute('update students set name="sathwik" where roll_no="102"')
x=cur.execute('select * from students')
print(x.fetchall())
con.commit()
print(x)