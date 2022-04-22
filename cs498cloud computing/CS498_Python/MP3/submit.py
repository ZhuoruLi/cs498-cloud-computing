import requests
import json
import uuid

url = "https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp3-autograder-2022-spring"

payload = {
	"graphApi": "https://4q7hvrjf5l.execute-api.us-east-1.amazonaws.com/tst",
	"botName": "ScheduleAppointment", 
	"botAlias": "mpthree_bot",
	"identityPoolId": "us-east-1:6a78d31c-f586-47c3-96ea-9140580d533a",
	"accountId": "369509601855",
	"submitterEmail": "lx6@illinois.edu",
	"secret": "yX8XhC2FHg1CiZaG",
	"region": "us-east-1"
    }

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)