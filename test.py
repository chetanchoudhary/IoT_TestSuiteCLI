import requests
import json

url = 'http://127.0.0.1:5000/api/v1/sensors'

headers = {
    'Accept': 'application/json',
    'Content-Type': "application/json",
    'cache-control': "no-cache",
}


def getSensors():
    result = requests.get(url, headers=headers)
    resultJson = json.dumps(result.json(), indent=4, sort_keys=True)
    print(help(result))
    return resultJson


def startSimulation(name):
    try:
        print("Finding your Sensor...")
        r = requests.post(url+'/'+name, headers=headers)
        print(r.json()['message'])
    except Exception as e:
        print(e)


startSimulation("ptcDevice")
