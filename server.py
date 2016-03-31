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
from flask import Flask, render_template, g, request
from flask.ext.socketio import SocketIO, send, emit
import math
import random
import threading
from multiprocessing import Process

# Global variables
app = Flask(__name__)
app.config['SECRET_KEY'] = 'bicamon'
socketio = SocketIO(app)

DATABASE = 'db/cells.db'

request_permission = {}

send_cells = {}
send_links = []
send_c_links = []

# Database Functions
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = make_dicts
    return db

def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

def query_db(query, args=(), one=False):
    cur = get_db().execute(query ,args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

# Request validation
def reset_permission():
    global request_permission
    for k in request_permission.keys():
        request_permission[k] = True
    t = threading.Timer(1.0, reset_permission)
    t.start()


# Initialize
def initialize():
    with app.app_context():
        # Global variables
        global request_permission
        global send_cells
        global send_links
        global send_c_links

        # Get data from database
        cellnames = query_db('select name from cells')
        links = query_db('select * from links')
        contra_links = query_db('select * from contra_links')

        # Set data
        for cellname in cellnames:
            name = cellname["name"]
            request_permission[name] = True
            send_cells[name] = query_db('select fullname,region,voxel,x,y,z from cells where name="%s"' % name)[0]

        for link in links:
            root_coordinate = query_db('select * from cells where name="%s"' % link["root"])
            dest_coordinate = query_db('select * from cells where name="%s"' % link["dest"])
            if len(root_coordinate) != 0 and len(dest_coordinate) != 0:
                send_links.append(link)

        for link in contra_links:
            root_coordinate = query_db('select * from cells where name="%s"' % link["root"])
            dest_coordinate = query_db('select * from cells where name="%s"' % link["dest"])
            if len(root_coordinate) != 0 and len(dest_coordinate) != 0:
                send_c_links.append(link)


# Routing Functions
@app.route('/')
def index():
    return render_template('index.html', cells=send_cells, links=send_links, c_links=send_c_links)

@app.route('/api', methods=['GET', 'POST'])
def api():
    # Global variables
    global request_permission

    if request.method == 'POST':
        data =  request.json
        data_name = []
        name = query_db('select name from cells where name="%s"' % data["cells"][0])
        if len(name) != 0 and request_permission[name[0]["name"]]:
            data_name.append(name[0]["name"])
            request_permission[name[0]["name"]] = False
        if len(data_name) != 0:
            socketio.emit('activation', data_name)
        return "Request was sended.\n"
    else:
        return "Request was aborted.\n"

# Main process
if __name__ == '__main__':
    # Initialize
    initialize()

    # Permission control
    t = threading.Thread(target=reset_permission)
    t.start()
    
    # Run
    app.debug = True
    socketio.run(app)
