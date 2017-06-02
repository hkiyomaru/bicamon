import argparse

import threading
import pandas as pd

from flask import Flask, render_template, request
from flask.ext.socketio import SocketIO


# parse command line argument
parser = argparse.ArgumentParser()
parser.add_argument('--light-mode', dest='light_mode', action='store_true',
                    help='reduce links to draw')
args = parser.parse_args()

# server settings
app = Flask(__name__)
app.config['SECRET_KEY'] = 'bicamon'
socketio = SocketIO(app)

# path to database
PATH_CELLS = 'db/cells.csv'
PATH_LINKS = 'db/links.csv'
PATH_C_LINKS = 'db/contra-links.csv'

# shared variables
cell_list = []  # a list of cells
send_cells = {}  # a dictionary that maps name into side information
send_links = []  # a list which includes `root`, `dest`, and `weight`
send_c_links = []  # a list which includes `root`, `dest`, and `weight`
unable_to_send = []  # a list of cells which have been sent to the viewer


def reset_permission():
    """Clear `unable_to_send`."""
    global unable_to_send
    unable_to_send = []
    t = threading.Timer(1.0, reset_permission)
    t.start()


def initialize():
    """Extract information from database."""
    with app.app_context():
        # Global variables
        global unable_to_send
        global send_cells
        global send_links
        global send_c_links

        cells_cols = ['name', 'fullname', 'region', 'voxel', 'x', 'y', 'z']
        cells = pd.read_table(PATH_CELLS, sep=',', names=cells_cols)

        links_cols = ['root', 'dest', 'weight']
        links = pd.read_table(PATH_LINKS, sep=',', names=links_cols)
        contra_links = pd.read_table(PATH_C_LINKS, sep=',', names=links_cols)

        for index, cell in cells.iterrows():
            name = cell['name']
            cell_list.append(name)
            send_cells[name] = dict(cell[1:])

        for index, link in links.iterrows():
            if link['root'] in list(cells['name']) and link['dest'] in list(cells['name']):
                if args.light_mode:
                    if link['weight'] > 0.1:
                        send_links.append(dict(link))
                else:
                    send_links.append(dict(link))

        for index, link in contra_links.iterrows():
            if link['root'] in list(cells['name']) and link['dest'] in list(cells['name']):
                if args.light_mode:
                    if link['weight'] > 0.1:
                        send_c_links.append(dict(link))
                else:
                    send_c_links.append(dict(link))


# Routing Functions
@app.route('/')
def index():
    """Returns `index.html`."""
    return render_template('index.html', cells=send_cells,
                           links=send_links, c_links=send_c_links)


@app.route('/api', methods=['GET', 'POST'])
def api():
    """Accept POST request and send requests to BiCAmon."""
    global unable_to_send

    if request.method == 'POST':
        data = request.json
        data_name = []
        for name in data['cells']:
            if name in cell_list and name not in unable_to_send:
                data_name.append(name)
                unable_to_send.append(name)
                socketio.emit('activation', data_name)
            else:
                continue
        message = "Request was sended.\n"
    else:
        message = "Request was aborted.\n"

    return message


if __name__ == '__main__':
    # extract information from db
    initialize()

    # control traffic
    t = threading.Thread(target=reset_permission)
    t.start()

    # launch an app
    socketio.run(app)
