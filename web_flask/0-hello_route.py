#!/usr/bin/python3

from flask import Flask
"""
    Imports the Flask class from the flask module.
    Flask is used to create a web application instance.
"""
app = Flask(__name__)
"""
    Creates a Flask application instance.
    __name__ is the name of the current Python module.
    The instance is used to handle requests and define routes.
"""


@app.route("/")
def hello_hbnb():

    """
    Defines a route handler function.
    Returns a greeting message for the /hbnb route.
    """
    return "<p>Hello HBNB!<p>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

