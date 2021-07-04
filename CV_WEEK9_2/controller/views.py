from flask import render_template, request
from PIL import Image
from service import utils

def index():
    return render_template("index.html")

def faceapp():
    return render_template("faceapp.html")

def detection():
    if request.method == "POST":
        f = request.files["image"]
        filename = f.filename
        path = "./static/uploads/" + filename
        f.save(path)
        w = getwidth(path)
        utils.pipeline_model(path, filename, color="bgr")

        return render_template("detection.html", fileupload=True, img_name=filename, w=w)

    return render_template("detection.html", fileupload=False, img_name="")

def getwidth(path):
    img = Image.open(path)
    size = img.size # width and height
    aspect = size[0] / size[1] # width / height
    w = 300 * aspect
    return int(w)