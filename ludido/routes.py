from flask import render_template
from ludido import app, db

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/activities")
def activities():
    return render_template("activities.html")

@app.route("/index")
def index():
    return render_template("index.html")