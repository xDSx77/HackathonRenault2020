import unittest
from ecosystem_api import Ecosystem
import requests


class MyTestCase(unittest.TestCase):
    def test_get_info(self):
        e = Ecosystem("http://team09.xp65.renault-digital.com", "None")
        print(e.get_agent_info())
        print(e.get_pollution())
        print(e.get_traffic())
        print(e.get_weather())
        print(e.get_metro_stations())
        print(e.get_closed_roads_walk())
        print(e.get_closed_roads_metro())

    def test_get_all_vehicles_info(self):
        e = Ecosystem("http://team09.xp65.renault-digital.com", "None")
        print(e.get_all_vehicles_info())

    def test_get_vehicle(self):
        e = Ecosystem("http://team09.xp65.renault-digital.com", "None")
        print(e.get_all_vehicles_info(), "")

    def test_get_graph(self):
        e = Ecosystem("http://team09.xp65.renault-digital.com", "None")
        print("Bike:")
        print(e.get_graph_bike())
        print("Metro:")
        print(e.get_graph_metro())
        print("Car:")
        print(e.get_graph_car())
        print("Walk:")
        print(e.get_graph_walk())

    def test_get_neighbours(self):
        e = Ecosystem("http://team09.xp65.renault-digital.com", "None")
        print(e.get_neighbours())
        print(e.get_neighbours_metro())
        print(e.get_neighbours_walk())

    def test_shortest_path(self):
        e = Ecosystem("http://team09.xp65.renault-digital.com", "None")
        print(e.get_shortest_path_walk({"x": 15.8, "y": 5.6}, {"x": 18.2, "y": 3.8}))


if __name__ == '__main__':
    unittest.main()
