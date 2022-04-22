# from re import S
# from urllib import request
from flask import Flask, request

app = Flask(__name__)

seednumber = 0
@app.route("/", methods=['POST', 'GET'])
# def hello_world():
#     return "<p>Hello, World!</p>"

def webServer():
    global seednumber
    if request.method == 'POST':
        seednumber = request.json["num"]
        # return seednumber
    elif request.method == 'GET':
        # s = ""
        # s = str(request.json["num"])
        return str(seednumber)

if __name__ == '__main__':
    app.run(debug=True)