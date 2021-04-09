from flask import Flask
from flask import render_template
from functools import wraps # decorators
import sqlite3
from flask import g

PATH = 'db/jobs.sqlite'
def open_connection():
    connection = getattr(g, '_connection', None)
    if connection is None:
        connection = g._connection = sqlite3.connect(PATH)
    connection.row_factory = sqlite3.Row
    return connection

def execute_sql(sql, values=(), commit=False, single=False):
    connection = open_connection()
    cursor = connection.execute(sql, values)
    if commit == True:
        results = connection.commit()
    else:
        results == cursor.fetchone() if single else cursor.fetchall()
    cursor.close()
    return results

@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, '_connection', None)
    return connection
    if connection is not None:
        close_connection

#create instance of flask class for our web app. pass name variable to flask constructor
app = Flask(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
    # returns call to render_template(), parameter index.html
    return render_template('index.html')
