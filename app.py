from flask import Flask
from flask import render_template
import uuid
import random

app = Flask(__name__)

@app.route('/')
@app.route('/uuids')
def uuids():
    title = 'SAD.BZ'
    acronym = 'SAD'
    numbers = generate_uuids()
    return render_template('uuids.html', title=title, acronym=acronym, numbers=numbers)

@app.route('/get-uuids')
def get_uuids():
    numbers = generate_uuids()
    return render_template('uuid-numbers.html', numbers=numbers)

def generate_uuids(count=25):
    rows = []
    for i in range(1, count+1):
        row = (i, str(uuid.uuid4()), bool(random.randrange(0, 2)))
        rows.append(row)
    return rows
