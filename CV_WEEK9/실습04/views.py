from flask import render_template, request

def index():

    if request.method == "POST":
        f = request.files["upload"]
        f.save("./uploads/" + f.filename)
        print("파일이 잘 저장되었습니다")
        
        return render_template("index.html", upload=True, fname=f.filename)

    return render_template("index.html", upload=False)