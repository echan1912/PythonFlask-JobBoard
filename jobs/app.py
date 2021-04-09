from flask import Flask 
from flask import render_template
import sqlite3
from flask import g



app = Flask(__name__)
def open_connection():
    getattr(g._connection, None)
    
   
        
    
     

def execute_sql(sql, values=(), commit=False, single=False):
    connection = open_connection
    cursor = execute_sql(connection, sql, values)
    if commit is True:
        
     
        results = cursor.fetchone() if single else cursor.fetchall()
        
        return results

@app.teardown_appcontext
def close_connection(exception):
    getattr(g,'_connection', None)
   

@app.route('/')
@app.route('/jobs')
def jobs():
    return render_template('index.html')

