from flask import render_template

def base():
    return render_template("base.html")

def index():
    return render_template("index.html")

def index2():
    return render_template("index2.html")

def index3():
    return render_template("index3.html")

