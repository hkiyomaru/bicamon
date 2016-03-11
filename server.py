import sqlite3
from flask import Flask, render_template, g

app = Flask(__name__)
DATABASE = 'db/cells.db'

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

@app.route('/')
def index():
    # for cell in query_db('select * from cells'):
    #     print cell['name']
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
