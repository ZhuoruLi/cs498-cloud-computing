import requests
import json

url = 'https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp2-autograder-2022-spring'

payload = {
		'ip_address1': "44.203.95.143:5000", # <insert ip address:port of first EC2 instance>, 
		'ip_address2': "34.224.97.149:5000", # <insert ip address:port of secong EC2 instance>,
		'load_balancer' : "loadbalancer-645341340.us-east-1.elb.amazonaws.com",# <insert address of load balancer>,
		'submitterEmail': "lx6@illinois.edu",# <insert your coursera account email>,
		'secret':  "d7rJK9utyrKUvjy0"# <insert your secret token from coursera>
		}

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)