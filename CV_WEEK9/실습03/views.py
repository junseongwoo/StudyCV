from flask import render_template, request
from flask import redirect, url_for
import json

def index():
    if request.method == "POST":
        first_name = request.form["first"]
        last_name = request.form["last"]
        email_id = request.form["email"]

        data = {
            "first" : first_name,
            "last_name" : last_name,
            "email" : email_id
        }

        return redirect(url_for("response", data=json.dumps(data)))

    return render_template("index.html")

def response(data):
    js_data = json.loads(data)
    data = dict(js_data)
    print(data)
    return render_template("response.html", data=data)