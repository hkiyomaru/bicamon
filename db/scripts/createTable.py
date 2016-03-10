import sqlite3

conn = sqlite3.connect('../cells.db')

sql = u"""
create table cells (
  name varchar(10),
  x integer,
  y integer,
  z integer
);
"""

conn.execute(sql)

conn.close()
