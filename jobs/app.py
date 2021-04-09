from flask import Flask
from flask import render_template

#create instance of flask class for our web app. pass name variable to flask constructor
app = Flask(__name__)

def jobs():
    # returns call to render_template(), parameter index.html
    return render_template('index.html')
