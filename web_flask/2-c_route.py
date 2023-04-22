#!/usr/bin/python3
""" Starts a Flask web application."""
from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ home view that return 'Hello HBNB'."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ hbnb view that returns 'HBNB'."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def croute(text):
    """croute view return 'c <text>'."""
    return f"C {text.replace('_',' ')}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
