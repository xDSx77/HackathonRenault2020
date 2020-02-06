import requests
import json
import logging


class Ecosystem:
    def __init__(self, url: str):
        # URL
        self.url = url
        # AGENT
        self.agent_situation = "/api/agent/api/user/situation/last"
        # CONTEXT
        self.weather = "/api/context/api/context/weather/current"
        self.pollution = "/api/context/api/context/air/current"
        # GRAPH
        self.graph_bike = "/api/graph/processed/bike.json"
        self.graph_car = "/api/graph/processed/vehicule.json"
        self.graph_metro = "/api/graph/processed/subway.json"
        self.graph_walk = "/api/graph/processed/walk.json"
        # NEIGHBOURS
        self.neighbours = "/api/graph/processed/neighbours.json"
        self.neighbours_metro = "/api/graph/processed/subway_neighbours.json"
        self.neighbours_walk = "/api/graph/processed/walk_neighbours.json"
        # SHORTEST PATH
        self.shortest_path_bike = "/api/graph/road_graph/shortest_path/bike"
        self.shortest_path_car = "/api/graph/road_graph/shortest_path/car"
        self.shortest_path_metro = "/api/graph/road_graph/shortest_path/subway"
        self.shortest_path_walk = "/api/graph/road_graph/shortest_path/walk"
        # METRO STATIONS
        self.metro_stations = "/api/graph/subway/stations"
        # TRAFFIC
        self.traffic = "/api/graph/road_graph/traffic_conditions"
        # CLOSED ROADS
        self.closed_roads_car = "/api/graph/road_graph/roads_status/car"
        self.closed_roads_bike = "/api/graph/road_graph/roads_status/bike"
        self.closed_roads_walk = "/api/graph/road_graph/roads_status/walk"
        self.closed_roads_metro = "/api/graph/road_graph/line_state"
        # VEHICLES
        self.vehicles_info = "/api/vehicle/api/v1/vehicles"

        # DEV ROUTES
        self.reset_walk_roads = "/api/graph/road_graph/reset_graph/walk"
        self.reset_bike_roads = "/api/graph/road_graph/reset_graph/bike"
        self.reset_car_roads = "/api/graph/road_graph/reset_graph/car"
        self.reset_metro_roads = "/api/graph/road_graph/reset_graph/subway"

    def get_agent_info(self) -> dict:
        route = self.url + self.agent_situation
        response = requests.get(url=route)
        if response.status_code != 200:
            logging.debug("ECOSYSTEM: REQUEST FAILED")
            return {}

        return response.json()

    def get_weather(self) -> dict:
        route = self.url + self.weather
        response = requests.get(url=route)
        if response.status_code != 200:
            logging.debug("ECOSYSTEM: REQUEST FAILED")
            return {}

        return response.json()

    def get_pollution(self) -> dict:
        route = self.url + self.pollution
        response = requests.get(url=route)
        if response.status_code != 200:
            logging.debug("ECOSYSTEM: REQUEST FAILED")
            return {}

        return response.json()

    def get_graph_car(self) -> dict:
        route = self.url + self.graph_car
        response = requests.get(url=route)
        if response.status_code != 200:
            logging.debug("ECOSYSTEM: REQUEST FAILED")
            return {}

        return response.json()

    def get_graph_bike(self) -> dict:
        route = self.url + self.graph_bike
        response = requests.get(url=route)
        if response.status_code != 200:
            logging.debug("ECOSYSTEM: REQUEST FAILED")
            return {}

        return response.json()

    def get_graph_walk(self) -> dict:
        route = self.url + self.graph_walk
        response = requests.get(url=route)
        if response.status_code != 200:
            logging.debug("ECOSYSTEM: REQUEST FAILED")
            return {}

        return response.json()

    def get_graph_metro(self) -> dict:
        route = self.url + self.graph_metro
        response = requests.get(url=route)
        if response.status_code != 200:
            logging.debug("ECOSYSTEM: REQUEST FAILED")
            return {}

        return response.json()

    def get_neighbours(self) -> dict:
        route = self.url + self.neighbours
        response = requests.get(url=route)
        if response.status_code != 200:
            logging.debug("ECOSYSTEM: REQUEST FAILED")
            return {}

        return response.json()

    def get_neighbours_metro(self) -> dict:
        route = self.url + self.neighbours_metro
        response = requests.get(url=route)
        if response.status_code != 200:
            logging.debug("ECOSYSTEM: REQUEST FAILED")
            return {}

        return response.json()

    def get_neighbours_walk(self) -> dict:
        route = self.url + self.neighbours_walk
        response = requests.get(url=route)
        if response.status_code != 200:
            logging.debug("ECOSYSTEM: REQUEST FAILED")
            return {}

        return response.json()

    def get_shortest_path_walk(self, src: dict, dst: dict) -> dict:
        route = self.url + self.shortest_path_walk

        payload = {
            "departure": src,
            "arrival": dst
        }

        response = requests.post(url=route, json=payload)
        if response.status_code != 200:
            logging.debug("ECOSYSTEM: REQUEST FAILED")
            return {}

        return response.json()

    def get_shortest_path_metro(self, src: dict, dst: dict) -> dict:
        route = self.url + self.shortest_path_metro

        payload = {
            "departure": src,
            "arrival": dst
        }

        response = requests.post(url=route, json=payload)
        if response.status_code != 200:
            logging.debug("ECOSYSTEM: REQUEST FAILED")
            return {}

        return response.json()

    def get_shortest_path_car(self, src: dict, dst: dict, vehicles: list) -> dict:
        route = self.url + self.shortest_path_car

        payload = {
            "departure": src,
            "arrival": dst,
            "vehicles": vehicles
        }

        response = requests.post(url=route, json=payload)
        if response.status_code != 200:
            logging.debug("ECOSYSTEM: REQUEST FAILED")
            return {}

        return response.json()

    def get_shortest_path_bike(self, src: dict, dst: dict) -> dict:
        route = self.url + self.shortest_path_bike

        payload = {
            "departure": src,
            "arrival": dst
        }

        response = requests.post(url=route, json=payload)
        if response.status_code != 200:
            logging.debug("ECOSYSTEM: REQUEST FAILED")
            return {}

        return response.json()

    def get_metro_stations(self) -> dict:
        route = self.url + self.metro_stations
        response = requests.get(url=route)
        if response.status_code != 200:
            logging.debug("ECOSYSTEM: REQUEST FAILED")
            return {}


        return response.json()

    def get_traffic(self) -> dict:
        route = self.url + self.traffic
        response = requests.get(url=route)
        if response.status_code != 200:
            logging.debug("ECOSYSTEM: REQUEST FAILED")
            return {}

        return response.json()

    def get_closed_roads_walk(self) -> dict:
        route = self.url + self.closed_roads_walk
        response = requests.get(url=route)
        if response.status_code != 200:
            logging.debug("ECOSYSTEM: REQUEST FAILED")
            return {}

        return response.json()

    def get_closed_roads_bike(self) -> dict:
        route = self.url + self.closed_roads_bike
        response = requests.get(url=route)
        if response.status_code != 200:
            logging.debug("ECOSYSTEM: REQUEST FAILED")
            return {}

        return response.json()

    def get_closed_roads_car(self) -> dict:
        route = self.url + self.closed_roads_car
        response = requests.get(url=route)
        if response.status_code != 200:
            logging.debug("ECOSYSTEM: REQUEST FAILED")
            return {}

        return response.json()

    def get_closed_roads_metro(self) -> dict:
        route = self.url + self.closed_roads_metro
        response = requests.get(url=route)
        if response.status_code != 200:
            logging.debug("ECOSYSTEM: REQUEST FAILED")
            return {}

        return response.json()

    def get_all_vehicles_info(self) -> dict:
        route = self.url + self.vehicles_info
        response = requests.get(url=route)
        if response.status_code != 200:
            logging.debug("ECOSYSTEM: REQUEST FAILED")
            return {}

        return response.json()

    def get_vehicle_info(self, id: str) -> dict:
        route = self.url + self.vehicles_info + "/" + id
        response = requests.get(url=route)
        if response.status_code != 200:
            logging.debug("ECOSYSTEM: REQUEST FAILED")
            return {}

        return response.json()

    def reset_road_walk(self) -> dict:
        route = self.url + self.reset_walk_roads
        response = requests.get(url=route)
        if response.status_code != 200:
            logging.debug("ECOSYSTEM: REQUEST FAILED")
            return {}

        return response.json()

    def reset_road_car(self) ->  dict:
        route = self.url + self.reset_car_roads
        response = requests.get(url=route)
        if response.status_code != 200:
            logging.debug("ECOSYSTEM: REQUEST FAILED")
            return {}

        return response.json()

    def reset_road_bike(self) -> dict:
        route = self.url + self.reset_bike_roads
        response = requests.get(url=route)
        if response.status_code != 200:
            logging.debug("ECOSYSTEM: REQUEST FAILED")
            return {}

        return response.json()

    def reset_road_metro(self) -> dict:
        route = self.url + self.reset_metro_roads
        response = requests.get(url=route)
        if response.status_code != 200:
            logging.debug("ECOSYSTEM: REQUEST FAILED")
            return {}

        return response.json()