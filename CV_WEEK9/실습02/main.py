from flask import Flask
import views

app = Flask(__name__)

app.add_url_rule("/base", "base", views.base)
app.add_url_rule("/index", "index", views.index)
app.add_url_rule("/index2", "index2", views.index2)
app.add_url_rule("/index3", "index3", views.index3)

if __name__ == "__main__":
    app.run(debug=True)