#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """A route that displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """A route that displays 'HBNB'"""
    return "Hello HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """A route that displays c text"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/<text>", strict_flashes=False)
@app.route("/python", strict_flashes=False)
def python_text(text="is cool"):
    """A route that displays python text"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
