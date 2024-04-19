#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask
from urllib.parse import unquote
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """A route that displays Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes-False)
def hbnb():
    """A route that displays HBNB"""
    return "Hello HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """A route that displays c text"""
    text: unquote(text).replace('_', ' ')
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
