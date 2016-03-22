#!/usr/bin/env python
import csv
import sqlite3

conn = sqlite3.connect('cells.db')

csvReader = csv.reader(open('seeds/cells.csv', 'rb'))

sql = u"insert into cells values (?, ?, ?, ?, ?, ?, ?, ?)"
for row in csvReader:
    try:
        conn.execute(sql, (None, row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
    except:
        pass

conn.commit()

csvReader = csv.reader(open('seeds/links.csv', 'rb'))

sql = u"insert into links values (?, ?, ?, ?)"
for row in csvReader:
    try:
        conn.execute(sql, (None, row[0], row[1], row[2]))
    except:
        pass

conn.commit()

csvReader = csv.reader(open('seeds/contra-links.csv', 'rb'))

sql = u"insert into contra_links values (?, ?, ?, ?)"
for row in csvReader:
    try:
        conn.execute(sql, (None, row[0], row[1], row[2]))
    except:
        pass

conn.commit()

conn.close()
