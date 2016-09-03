import sqlite3
from flask import Flask, render_template, g, request
from flask.ext.socketio import SocketIO, send, emit

import commands
import threading

import argparse

# Global variables
app = Flask(__name__)
app.config['SECRET_KEY'] = 'bicamon'
socketio = SocketIO(app)

DATABASE = 'db/cells.db'

request_permission = []

send_cells = {}
send_links = []
send_c_links = []


# Parse command line argument
parser = argparse.ArgumentParser()
parser.add_argument('--no-db-build', dest='no_build_db', action='store_true', help='skip db-build process')
parser.add_argument('--light-mode', dest='light_mode', action='store_true', help='reduce links to draw')
args = parser.parse_args()

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
    request_permission = []
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

        # Build database
        if args.no_build_db:
            pass
        else:
            check = commands.getoutput("./db/makedb.sh")

        # Get data from database
        cellnames = query_db('select name from cells')
        links = query_db('select * from links')
        contra_links = query_db('select * from contra_links')

        # Set data
        for cellname in cellnames:
            name = cellname["name"]
            send_cells[name] = query_db('select fullname,region,voxel,x,y,z from cells where name="%s"' % name)[0]

        for link in links:
            root_coordinate = query_db('select * from cells where name="%s"' % link["root"])
            dest_coordinate = query_db('select * from cells where name="%s"' % link["dest"])
            if len(root_coordinate) != 0 and len(dest_coordinate) != 0:
                if args.light_mode:
                    if link['weight'] > 0.1:
                        send_links.append(link)
                else:
                    send_links.append(link)

        for link in contra_links:
            root_coordinate = query_db('select * from cells where name="%s"' % link["root"])
            dest_coordinate = query_db('select * from cells where name="%s"' % link["dest"])
            if len(root_coordinate) != 0 and len(dest_coordinate) != 0:
                if args.light_mode:
                    if link['weight'] > 0.1:
                        send_c_links.append(link)
                else:
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
        if len(name) != 0 and not name[0]["name"] in request_permission:
            data_name.append(name[0]["name"])
            request_permission.append(name[0]["name"])
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
    socketio.run(app)
