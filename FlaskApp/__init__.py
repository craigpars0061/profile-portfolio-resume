#!/usr/bin/env python3

from flask import Flask, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

# Base route.
@app.route("/")
def startMain():
    return render_template("main.html")

# The pendulum photography portfolio page.
@app.route('/pendulum/')
def portfolio():
    return render_template("portfolio.html")

if __name__ == "__main__":
    app.run()
