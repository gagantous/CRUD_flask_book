import sqlite3

conn = sqlite3.connect('employee.db')

c = conn.cursor()

# c.execute("CREATE table employee (first text, last text, pay integer)")

#query = c.execute("INSERT INTO employee VALUES (98091290, '121313', 100) WHERE ")
try:
    query = c.execute("INSERT INTO employee VALUES ('Test', 'Abdul', 100000)")
except:
    print("Query tidak dapat dijalankan")
finally:
    c.execute("Select * from employee")
    print(c.fetchall())
    result = c.fetchone()
conn.commit()
conn.close()

#for res in result:
 #  print (res,sep='\n\n')
