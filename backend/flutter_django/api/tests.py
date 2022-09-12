#from django.test import TestCase

# Create your tests here.
import requests
import json

url = "http://192.168.10.10:8000/api/generatetoken"
data = {"username":"test","password":"test"}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(data), headers=headers)
print(r.text)
