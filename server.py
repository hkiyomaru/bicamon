import sqlite3
from flask import Flask, render_template, g
from flask.ext.socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mouse-brain-visualization'
socketio = SocketIO(app)
DATABASE = 'db/cells.db'

# ----------- DB -----------
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

# ----------- WebSockets -----------
# @socketio.on('message')
# def handle_message(message):
#     send(message)

# @socketio.on('json')
# def handle_json(json):
#     send(json, json=True)

# @socketio.on('activation')
# def send_activation(json):
#     emit('activation', json, callback=ack)

# @socketio.on_error()
# def error_handler(e):
#     print e

# ----------- Routing -----------
@app.route('/')
def index():
    cells = query_db('select * from cells')
    return render_template('index.html', cells = cells)

@app.route('/api')
def api():
    socketio.emit('activation', [1])
    return "Request was sended.\n"

if __name__ == '__main__':
    app.debug = True
    socketio.run(app)
