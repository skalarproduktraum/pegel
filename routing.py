import os
from flask import Flask

app = Flask(__name__, static_folder="static")

@app.route('/')
def hello():
    return '<a href="501010/">Schoena</a>, <a href="501060/">Dresden</a>, <a href="501080/">Meissen</a>'
