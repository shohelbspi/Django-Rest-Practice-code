import requests
import json

URL = "http://127.0.0.1:8000/student-api/"

def getData(id=None):
    data = {}
    if id is not None:
        data = {'id':id}

    json_data = json.dumps(data)
    headers = {'content-type':'application/json'}
    r = requests.get(url=URL,headers=headers,data=json_data)
    data = r.json()
    print(data)

# getData(1)

def postData():
    data = {
        'name':"Ridoy Khan",
        'roll': 123518,
        'dep':"Music",
    }
    headers = {'content-type':'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=URL,headers=headers, data=json_data)
    data = r.json()
    print(data)

# postData()

def updateData():
    data = {
        'id':3,
        'name':"Sai Pallavi",
        "dep":'Actor',
    }
    headers = {'content-type':'application/json'}

    json_data = json.dumps(data)
    r = requests.put(url=URL,headers=headers,data=json_data)
    data = r.json()
    print(data)

# updateData()
    
def deleteData():
    data = {
        'id':4,
    }
    headers = {'content-type':'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url=URL,headers=headers,data=json_data)
    data = r.json()
    print(data)

deleteData()

