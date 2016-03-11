#!/usr/bin/env python
import sqlite3

conn = sqlite3.connect('cells.db')

sql = u"""
create table cells (
  id integer PRIMARY KEY AUTOINCREMENT,
  name varchar(10) UNIQUE,
  x integer,
  y integer,
  z integer
);
"""

conn.execute(sql)

conn.close()
