#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route("/")
def homepage():
    return "Hello, I love Python"

if __name__ == "__main__":
    app.run()
