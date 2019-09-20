import requests
import fire
import json
url = 'http://127.0.0.1:5000/api/v1/sensors'

headers = {
    'Accept': 'application/json',
    'Content-Type': "application/json",
    'cache-control': "no-cache",
}


def getSensors():
    try:
        result = requests.get(url, headers=headers)
        resultJson = json.dumps(result.json(), indent=4, sort_keys=True)
        return resultJson
    except Exception as error:
        return error


def getSensorByName(name):
    try:
        result = requests.get(url+'/'+name, headers=headers)
        resultJson = json.dumps(result.json(), indent=4, sort_keys=True)
        if result.status_code == 404:
            return result.json()["message"]
        return resultJson
    except Exception as error:
        return error


def startSimulation(name):
    try:
        print("Finding your Sensor...")
        r = requests.post(url+'/'+name, headers=headers)
        print(r.json()['message'])
    except Exception as e:
        print(e)


def addSensorPTC(name, format, timeInterval, frequency, minRange, maxRange, broker, topic, appKey):

    connection = json.dumps(
        {"broker": broker, "topic": topic, "appKey": appKey})
    payload = {"name": name, "cloud": "thingworx", "connection": connection, "format": format,
               "timeInterval": timeInterval, "frequency": frequency, "minRange": minRange, "maxRange": maxRange}

    payload = json.dumps(payload)
    # print(payload)
    r = requests.post(url, data=payload, headers=headers)
    if r.status_code != 201:
        return r.json()["message"]
    else:
        print("Your Sensor has been created Successfully !")
        return r.json()


def addSensorAZURE():
    pass


def addSensorAWS():
    pass

# Update Sensor
# /api/v1/sensors/<string:name>/range


def updateSensorRange(name, minRange, maxRange):
    urlNew = url + '/' + name + '/' + 'range'
    payload = json.dumps({"minRange": minRange, "maxRange": maxRange})
    requests.put(urlNew, data=payload, headers=headers)


def updateFrequencyAndTimeInterval(name, frequency, timeInterval):
    urlNew = url + '/' + name + '/' + 'time_frequency'
    payload = json.dumps(
        {"frequency": frequency, "timeInterval": timeInterval})
    requests.put(urlNew, data=payload, headers=headers)


if __name__ == '__main__':
    fire.Fire()
