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


@app.route("/api/get/shortestpath", methods=['GET', 'POST'])
def get_shortest_paths() -> dict:
    """
    Get shortest path according to config file
    """
    mission_json = json.loads(subscribe_mission.subscribe_mission())
    with open("config.dev.json") as json_f:
        json_data = json.load(json_f)
    ecosystem = Ecosystem(json_data["url"])
    src_json = ecosystem.get_agent_info()
    # print("DATA: " + str(data['positions']))
    # filters = [request.form["filters"]]
    filters = []
    src = {"x": src_json['position']['x'], "y": src_json['position']['y']}
    dst = {"x": mission_json['positions'][0]['x'], "y": mission_json['positions'][0]['y']}
    # print(dst)
    with open("config.dev.json") as fp:
        data = json.load(fp)
        if "url" in data:
            url = data["url"]
        else:
            print("URL IS NOT IN CONFIG FILE")
            return {}

    return short.get_shortest_paths(src, dst, filters, url)


@app.route("/api/get_agent_info")
def get_agent_info():
    with open("config.dev.json") as json_f:
        json_data = json.load(json_f)
    ecosystem = Ecosystem(json_data["url"])
    return ecosystem.get_agent_info()


@app.root_path("/api/get_weather")
def get_weather() -> dict:
    with open("config.dev.json") as json_f:
        json_data = json.load(json_f)
    ecosystem = Ecosystem(json_data["url"])
    return ecosystem.get_weather()


@app.root_path("/api/get_pollution")
def get_pollution() -> dict:
    with open("config.dev.json") as json_f:
        json_data = json.load(json_f)
    ecosystem = Ecosystem(json_data["url"])
    return ecosystem.get_pollution()


@app.root_path("/api/get_graph_car")
def get_graph_car() -> dict:
    with open("config.dev.json") as json_f:
        json_data = json.load(json_f)
    ecosystem = Ecosystem(json_data["url"])
    return ecosystem.get_graph_car()


@app.root_path("/api/get_graph_bike")
def get_graph_bike() -> dict:
    with open("config.dev.json") as json_f:
        json_data = json.load(json_f)
    ecosystem = Ecosystem(json_data["url"])
    return ecosystem.get_graph_bike()


@app.root_path("/api/get_graph_walk")
def get_graph_walk() -> dict:
    with open("config.dev.json") as json_f:
        json_data = json.load(json_f)
    ecosystem = Ecosystem(json_data["url"])
    return ecosystem.get_graph_walk()


@app.root_path("/api/get_graph_metro")
def get_graph_metro() -> dict:
    with open("config.dev.json") as json_f:
        json_data = json.load(json_f)
    ecosystem = Ecosystem(json_data["url"])
    return ecosystem.get_graph_metro()


@app.root_path("/api/get_neighbours")
def get_neighbours() -> dict:
    with open("config.dev.json") as json_f:
        json_data = json.load(json_f)
    ecosystem = Ecosystem(json_data["url"])
    return ecosystem.get_neighbours()


@app.root_path("/api/get_neighbours_metro")
def get_neighbours_metro() -> dict:
    with open("config.dev.json") as json_f:
        json_data = json.load(json_f)
    ecosystem = Ecosystem(json_data["url"])
    return ecosystem.get_neighbours_metro()


@app.root_path("/api/get_neighbours_walk")
def get_neighbours_walk() -> dict:
    with open("config.dev.json") as json_f:
        json_data = json.load(json_f)
    ecosystem = Ecosystem(json_data["url"])
    return ecosystem.get_neighbours_walk()


@app.root_path("/api/get_metro_stations")
def get_metro_stations() -> dict:
    with open("config.dev.json") as json_f:
        json_data = json.load(json_f)
    ecosystem = Ecosystem(json_data["url"])
    return ecosystem.get_metro_stations()


@app.root_path("/api/get_traffic")
def get_traffic() -> dict:
    with open("config.dev.json") as json_f:
        json_data = json.load(json_f)
    ecosystem = Ecosystem(json_data["url"])
    return ecosystem.get_traffic()


@app.root_path("/api/get_closed_roads_walk")
def get_closed_roads_walk() -> dict:
    with open("config.dev.json") as json_f:
        json_data = json.load(json_f)
    ecosystem = Ecosystem(json_data["url"])
    return ecosystem.get_closed_roads_walk()


@app.root_path("/api/get_closed_roads_bike")
def get_closed_roads_bike() -> dict:
    with open("config.dev.json") as json_f:
        json_data = json.load(json_f)
    ecosystem = Ecosystem(json_data["url"])
    return ecosystem.get_closed_roads_bike()


@app.root_path("/api/get_closed_roads_car")
def get_closed_roads_car() -> dict:
    with open("config.dev.json") as json_f:
        json_data = json.load(json_f)
    ecosystem = Ecosystem(json_data["url"])
    return ecosystem.get_closed_roads_car()


@app.root_path("/api/get_closed_roads_metro")
def get_closed_roads_metro() -> dict:
    with open("config.dev.json") as json_f:
        json_data = json.load(json_f)
    ecosystem = Ecosystem(json_data["url"])
    return ecosystem.get_closed_roads_metro()


@app.root_path("/api/get_all_vehicles_info")
def get_all_vehicles_info() -> dict:
    with open("config.dev.json") as json_f:
        json_data = json.load(json_f)
    ecosystem = Ecosystem(json_data["url"])
    return ecosystem.get_all_vehicles_info()


