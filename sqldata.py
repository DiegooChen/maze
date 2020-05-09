# -*- encoding:utf-8 -*-

import sqlite3

con = sqlite3.connect('sqlite.db')

c = con.cursor()
c.execute('''CREATE TABLE CONFIG
        (ID TEXT PRIMARY KEY NOT NULL,
        )
    ''')