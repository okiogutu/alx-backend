#!/usr/bin/env python3
""" Basic simple flask app """

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """ page class root"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
