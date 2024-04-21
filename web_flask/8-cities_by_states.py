#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """A route that displays a HTML page with the State by Cities objects"""
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """A route that removes the current SQLAlchemy session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
