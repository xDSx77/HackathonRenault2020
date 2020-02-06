from rest.ecosystem_api import Ecosystem
from mqtt import subscribe_mission
from flask import Flask, request
import json
app = Flask(__name__)


@app.route("/api/subscribe_mission")
# Subscribe to the mission channel
def subscribe_mission_f():
    subscribe_mission()


@app.route("/api/get_agent_info")
def get_agent_info():
    with open("../config.dev.json") as json_f:
        json_data = json.load(json_f)
    ecosystem = Ecosystem(json_data["url"])
    return ecosystem.get_agent_info()
