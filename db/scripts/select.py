#!/usr/bin/env python
import csv
import sqlite3

conn = sqlite3.connect('../cells.db')

c = conn.cursor()

sql = u"select * from cells"

c.execute(sql)

for row in c:
    print row

conn.close()
