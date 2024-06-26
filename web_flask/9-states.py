#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """A route that displays a HTML page with the list of States objects"""
    states = storage.all("State")
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """A route that displays a HTML page with the id of the States objects"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """A route that removes the current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
