import os
from flask import Flask

app = Flask(__name__, static_folder="static")

@app.route('/')
def hello():
    return '<a href="static/501010/">Schoena</a>, <a href="static/501060/">Dresden</a>, <a href="static/501080/">Meissen</a>'
