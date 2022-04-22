import requests
import json
payload = {
        "USE_CACHE": "True",
        "REQUEST": "read",
        "SQLS": [1,2,3]
    }
api = "https://ctvfq2t08c.execute-api.us-east-1.amazonaws.com/mp6_tst"
r = requests.post(api, data=json.dumps(payload))
res = ""
res = r.json()['body']