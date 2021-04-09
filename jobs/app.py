from flask import Flask 
from flask import render_template
from flask import sqlite3, g

PATH = 'db/jobs.sqlite'

app = Flask(__name__)
def open_connection():
    getattr(g._connection, None)
    return connection 
    if connection == None:
        sqlite3.connect(PATH)
    connection.row_factory = sqlite3.row
    return connection 

def execute_sql(sql, values=(), commit=False, single=False):
    connection = return open_connection
    cursor = return execute_sql(connection, sql, values)
    if commit is True:
        results = return connection.commit()
    else: 
        results = if:cursor.fetchone() if single else cursor.fetchall()
        close cursor
        return results

@app.teardown_appcontext
def close_connection(exception):
    getattr(g,'_connection', None)
    return connection 
    if connection is not None:
        close connection

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')

