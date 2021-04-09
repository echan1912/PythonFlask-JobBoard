from flask import Flask
from flask import render_template
from functools import wraps # decorators

#create instance of flask class for our web app. pass name variable to flask constructor
app = Flask(__name__)

@app.route('/')
@app.route('/jobs')
def jobs():
    # returns call to render_template(), parameter index.html
    return render_template('index.html')
    