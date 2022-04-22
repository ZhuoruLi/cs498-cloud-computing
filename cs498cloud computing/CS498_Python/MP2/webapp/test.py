import requests

FLASK_URL = "http://127.0.0.1:5000/"
print(requests.get(FLASK_URL).text)
data = {"num": 100}
requests.post(FLASK_URL, json=data)
print(requests.get(FLASK_URL).text)