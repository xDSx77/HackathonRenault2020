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
        #print(e.get_all_vehicles_info())
        print(e.get_closed_roads_walk())
        print(e.get_graph_bike())
        print(e.get_graph_car())
        print(e.get_graph_bike())
        print(e.get_closed_roads_metro())
        print(e.get_neighbours())

    def test_shortest_path(self):
        e = Ecosystem("http://team09.xp65.renault-digital.com", "None")
        print(e.get_shortest_path_bike({ "x":15.79, "y":2.0 }, { "x":11.0, "y":2.0 }))
        print(e.get_shortest_path_metro({ "x":15.79, "y":2.0 }, { "x":11.0, "y":2.0 }))
        print(e.get_shortest_path_walk({ "x":15.79, "y":2.0 }, { "x":11.0, "y":2.0 }))
        print(e.get_shortest_path_car({ "x":15.79, "y":2.0 }, { "x":11.0, "y":2.0 }, [{ "id":"correl_1", "x":21.8, "y":5.6 },{ "id":"correl_2", "x":11.2, "y":0.2 }]))

if __name__ == '__main__':
    unittest.main()
