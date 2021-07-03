# main.py

from flask import Flask
import views

app = Flask(__name__)

app.add_url_rule("/", "index", views.index)
app.add_url_rule("/template/<name>/<int:marks>", "index_template", views.index_tem)
app.add_url_rule("/forloop", "index_for", views.index_for)

if __name__ == "__main__":
    app.run(debug=True)