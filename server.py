import sqlite3
from flask import Flask, render_template, g, request
from flask.ext.socketio import SocketIO, send, emit
import math
import random
import threading

# Global variables
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mouse-brain-visualization'
socketio = SocketIO(app)

DATABASE = 'db/cells.db'

original_request_permission = {}
request_permission = {}


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
    request_permission = dict(original_request_permission)
    t = threading.Timer(1.0, reset_permission)
    t.start()

# Routing Functions
@app.route('/')
def index():
    # Get data from database
    cellnames = query_db('select name from cells')
    links = query_db('select * from links')
    contra_links = query_db('select * from contra_links')
    
    # Data to send to view
    send_cells = {}
    send_links = []
    send_c_links = []
    global original_request_permission
    
    # Set data
    for cellname in cellnames:
        name = cellname["name"]
        original_request_permission[name] = True
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

    return render_template('index.html', cells=send_cells, links=send_links, c_links=send_c_links)

@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        data =  request.json
        data_name = []
        for d in data["cells"]:
            name = query_db('select name from cells where name="%s"' % d)
            if len(name) != 0:
                if request_permission[name[0]["name"]]:
                    data_name.append(name[0]["name"])
                    request_permission[name[0]["name"]] = False
        if len(data_name) != 0:
            socketio.emit('activation', data_name)
        return "Request was sended.\n"
    else:
        return "Request was aborted.\n"

# Main process
if __name__ == '__main__':
    # Permission
    reset_permission()

    # Run
    app.debug = True
    socketio.run(app)
