import sqlite3
from flask import Flask, render_template, g, request
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

# ----------- Routing -----------
@app.route('/')
def index():
    cells = query_db('select * from cells')
    return render_template('index.html', cells = cells)

@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'POST':
        data =  request.json
        data_index = []
        for d in data["cells"]:
            index = query_db('select id from cells where name="%s"' % d)
            if len(index) != 0:
                data_index.append(index[0]["id"] - 1)
        socketio.emit('activation', data_index)
        return "Request was sended.\n"
    else:
        return "No use to send request.\n"

if __name__ == '__main__':
    app.debug = True
    socketio.run(app)
