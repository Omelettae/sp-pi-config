import json
import requests

with open("config.json") as f:
    config = json.load(f)

register_url = f"{config['serverURL']}/api/registerSensor"

response = requests.post(
    register_url,
    json={
        "deviceUUID": config["deviceUUID"],
        "sensorType": config["sensorType"],
        "locationName": config["locationName"]
    }
)
