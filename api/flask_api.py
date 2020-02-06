from rest.ecosystem_api import Ecosystem
from mqtt import subscribe_mission
from flask import Flask, request
import json
import mqtt.mqtt_base as mqtt_base
import shortestpath.shortestpath as short
app = Flask(__name__)


@app.route("/api/subscribe_mission")
# Subscribe to the mission channel
def subscribe_mission_f():
    return subscribe_mission.subscribe_mission()


@app.route("/api/get_agent_info")
def get_agent_info():
    with open("config.dev.json") as json_f:
        json_data = json.load(json_f)
    ecosystem = Ecosystem(json_data["url"])
    return ecosystem.get_agent_info()


@app.route("/api/get/shortestpath", methods=['GET', 'POST'])
def get_shortest_paths() -> dict:
    """
    Get shortest path according to config file
    """
    data = subscribe_mission.subscribe_mission()
    print(data)
    filters = [request.form["filters"]]
    src = {"x": 0, "y": 0} # TODO get src coord
    dst = {"x": data["positions"]["x"], "y": data["positions"]["y"]}
    print(dst)
    with open("config.dev.json") as fp:
        data = json.load(fp)
        if "url" in data:
            url = data["url"]
        else:
            print("URL IS NOT IN CONFIG FILE")
            return {}

    return short.get_shortest_paths(src, dst, filters, url)
