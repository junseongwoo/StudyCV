# index.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "안녕하세요! "

@app.route("/route1")
def route1():
    return "새로운 경로1"

def route2():
    return "새로운 경로2"    
app.add_url_rule("/route2", "route2", route2)

@app.route("/<name>")
def variable(name):
    return "입력받은 변수는 {}입니다.".format(name)

@app.route("/blog/<int:blogid>")
def blog(blogid):
    return "이번 블로그의 아이디는 {}입니다.".format(blogid)

@app.route("/weight/<float:w>")
def weight(w):
    return "몸무게는 %s입니다."%w

if __name__ == "__main__": 
    app.run(debug=True)
