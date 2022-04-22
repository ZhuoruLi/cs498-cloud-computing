import requests
import json

url = 'https://ikm2evu584.execute-api.us-east-1.amazonaws.com/test/mp11-autograder'

payload = {
			"submitterEmail": "lx6@illinois.edu", # <insert your coursera account email>,
			"secret": "Z7HsDf8q8zU2aXaV", # <insert your secret token from coursera>,
			# "partId" : "G6U3L"
			"dbApi": "https://ctvfq2t08c.execute-api.us-east-1.amazonaws.com/mp6_tst"
		}
print(json.dumps(payload))
r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)