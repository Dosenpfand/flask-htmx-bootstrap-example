from flask import Flask
from flask import render_template
import uuid
import random

app = Flask(__name__)


@app.route('/')
def uuids():
    title = 'SAD.BZ'
    uuid_rows = generate_uuids()
    return render_template('uuids.html', title=title, uuid_rows=uuid_rows)


@app.route('/uuid-table')
def uuid_table():
    uuid_rows = generate_uuids()
    return render_template('uuid-table.html', uuid_rows=uuid_rows)


def generate_uuids(count=25):
    rows = []
    for i in range(1, count+1):
        row = (i, str(uuid.uuid4()), bool(random.randrange(0, 2)))
        rows.append(row)
    return rows
