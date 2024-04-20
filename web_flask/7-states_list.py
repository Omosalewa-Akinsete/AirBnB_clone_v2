#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage
from moels.state import State
app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exception):
    """A route that closes the storage on teardown"""
    storage.close()


@app.route("/states_list")
def states_list():
    """A route that displays a HTML page with the list of State objects"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
