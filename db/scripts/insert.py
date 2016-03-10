import csv
import sqlite3

conn = sqlite3.connect('../cells.db')

csvReader = csv.reader(open('../seeds/Isocortex.csv', 'rb'))

sql = u"insert into cells values (?, ?, ?, ?)"
for row in csvReader:
    conn.execute(sql, (row[0], row[1], row[2], row[3]))

conn.commit()

conn.close()
