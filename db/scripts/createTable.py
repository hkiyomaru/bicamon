#!/usr/bin/env python
import sqlite3

conn = sqlite3.connect('cells.db')

cur = conn.cursor()

cur.execute("""create table cells (id integer PRIMARY KEY AUTOINCREMENT,name varchar(10) UNIQUE,region varchar(30),voxel integer,x integer,y integer,z integer);""")

cur.execute("""create table links (id integer PRIMARY KEY AUTOINCREMENT,fromcell varchar(10),tocell varchar(10),weight float);""")

conn.close()
