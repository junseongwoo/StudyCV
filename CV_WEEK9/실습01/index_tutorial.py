# index.py

from flask import Flask

app = Flask(__name__)  # app이라는 Flaks 클래스 생성

# route() : 애플리케이션에게 url을 호출하면 그 url은
# 애플리케이션의 어디로 갈지 알려주는 함수
# app.route(url, options)
# "/" : 홈페이지의 루트, 

@app.route("/")  # @ : 함수의 기능을 추가해준다 
def index():
    return "안녕하세요! "

if __name__ == "__main__": # index.py의 entry point
    app.run(
        port=5500,
        debug=True
    )

# run() : 현재 실행하는 서버에 있는 애플리케이션을 실행
# run(
#   host=None,
#   port=None,
#   debug=None,
#   load_dotenv=True,
#   options
# )
# default host: 127.0.0.1 (localhost)
# default port : 5000
# default debug: False