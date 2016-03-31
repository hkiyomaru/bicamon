#!/usr/bin/env python

import csv
import sqlite3

conn = sqlite3.connect('../cells.db')

c = conn.cursor()

sql = u"select * from contra_links"

c.execute(sql)

for row in c:
    print row

conn.close()
