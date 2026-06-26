import json
import requests

with open("config.json") as f:
    config = json.load(f)

deviceUUID = config["deviceUUID"]
sensorType = config["sensorType"]
locationName = config["locationName"]

requests.post(
    "http://your-server:3000/api/registerSensor",
    json={
        "deviceUUID": deviceUUID,
        "sensorType": sensorType,
        "locationName": locationName
    }
)
