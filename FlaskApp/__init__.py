#!/usr/bin/env python3

from flask import Flask, render_template
app = Flask(__name__)

# Base route.
@app.route("/")
def startMain():
    return render_template("main.html")
   
# This seems to be the simple routing system.

@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run()
