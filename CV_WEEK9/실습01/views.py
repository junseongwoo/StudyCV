# views.py

from flask import render_template

def index():
    return "Views 방식의 홈페이지에 오신 것을 환영합니다."

def index_tem(name, marks):
    # marks = 49
    return render_template("index.html", name=name, marks = marks)

def index_for():
    data = {
        "통계" : 70,
        "머신러닝" : 50,
        "딥러닝" : 75, 
        "파이썬" : 20
    }
    return render_template("index_for.html", data=data)