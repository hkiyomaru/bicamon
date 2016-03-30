#!/usr/bin/env python

'''
The MIT License (MIT)

Copyright (c) 2016 Hirokazu Kiyomaru

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import sqlite3

conn = sqlite3.connect('cells.db')

cur = conn.cursor()

cur.execute("""create table cells (id integer PRIMARY KEY AUTOINCREMENT,name varchar(10) UNIQUE,fullname varchar(30),region varchar(30),voxel integer,x integer,y integer,z integer);""")

cur.execute("""create table links (id integer PRIMARY KEY AUTOINCREMENT,root varchar(10),dest varchar(10),weight float);""")

cur.execute("""create table contra_links (id integer PRIMARY KEY AUTOINCREMENT,root varchar(10),dest varchar(10),weight float);""")

conn.close()
