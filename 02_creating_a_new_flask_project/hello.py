from flask import Flask
import os  
app = Flask(__name__)


@app.route("/hello/")
def hello():
    return "<p>Hello</p>"