# -*- encoding:utf-8 -*-

import sqlite3

con = sqlite3.connect('maze.db')

def create_tables():


c = con.cursor()
# c.execute('''CREATE TABLE CONFIG
#         (ID TEXT PRIMARY KEY NOT NULL,
#         NAME TEXT NOT NULL,
#         AGE INT NOT NULL,
#         ADDRESS CHAR(50),
#         SALARY REAL);''')
# print('Table created successfully.')
# con.commit()
# con.close()

# c.execute("INSERT INTO CONFIG (ID, NAME, AGE, ADDRESS, SALARY) \
#           VALUES(1, 'Paul', 32, 'California', 20000.00)")
#
# c.execute("INSERT INTO CONFIG (ID, NAME, AGE, ADDRESS, SALARY) \
#           VALUES(2, 'Allen', 25, 'Texas', 15000.00)")
#
# c.execute("INSERT INTO CONFIG (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")
#
# c.execute("INSERT INTO CONFIG (ID,NAME,AGE,ADDRESS,SALARY) \
#       VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

c.execute('UPDATE CONFIG SET SALARY = 55000.00 WHERE ID = 1')
con.commit()


cursor = con.execute("SELECT id, name, address, salary  from CONFIG")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3], "\n")

print('Records created successfully')
con.close()
