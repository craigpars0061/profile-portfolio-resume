#!/usr/bin/env python3

from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def startMain():
    return render_template("main.html")

if __name__ == "__main__":
    app.run()