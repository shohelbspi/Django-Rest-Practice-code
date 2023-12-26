import requests
import json

URL = "http://127.0.0.1:8000/student-api/"

data = {
    'roll' : 2,
    'name':'Sompa Hossain',
    'dep' : "Nursing"
}

json_data = json.dumps(data)

r = requests.post(url=URL,data=json_data)

data = r.json()
print(data)