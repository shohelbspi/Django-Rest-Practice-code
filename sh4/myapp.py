import requests
import json

URL = "http://127.0.0.1:8000/student-api/"

def getData(id=None):
    data = {}
    if id is not None:
        data = {'id':id}

    json_data = json.dumps(data)
    r = requests.get(url=URL,data=json_data)
    data = r.json()
    print(data)

# getData(1)

def postData():
    data = {
        'name':"Ridoy Khan",
        'roll': 123518,
        'dep':"Music",
    }

    json_data = json.dumps(data)
    r = requests.post(url=URL,data=json_data)
    data = r.json()
    print(data)

# postData()

def updateData():
    data = {
        'id':3,
        'name':"Sai Pallavi",
        "dep":'Actor',
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL,data=json_data)
    data = r.json()
    print(data)

# updateData()
    
def deleteData():
    data = {
        'id':3,
    }
    json_data = json.dumps(data)
    r = requests.delete(url=URL,data=json_data)
    data = r.json()
    print(data)

deleteData()

