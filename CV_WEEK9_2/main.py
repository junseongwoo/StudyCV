from flask import Flask
from controller import views

app = Flask(__name__)

app.add_url_rule("/", "index", views.index)
app.add_url_rule("/faceapp", "faceapp", views.faceapp)
app.add_url_rule("/faceapp/detection", "detection", views.detection, methods = ['GET', 'POST'])

if __name__ == "__main__":
    app.run(debug=True)