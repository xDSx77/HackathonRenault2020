import unittest
import shortestpath

from ecosystem_api import Ecosystem

class MyTestCase(unittest.TestCase):
    def test_something(self):
        d = shortestpath.get_shortest_paths({"x": 15.8, "y": 5.6}, {"x": 18.2, "y": 3.8}, [], "http://team09.xp65.renault-digital.com")
        print(d)

    def test_with_print(self):
        d = shortestpath.get_shortest_paths({ "x":15.79, "y":2.0 }, {"x": 20.2, "y": 3.8}, [], "http://team09.xp65.renault-digital.com")
        for k, v in d.items():
            print(k, v)

    def test_metro(self):
        ecosystem = Ecosystem("http://team09.xp65.renault-digital.com", "env")

        src = { "x":15.79, "y":2.0 }
        dst = {"x": 20.2, "y": 3.8}

        path_subway = ecosystem.get_shortest_path_walk(src, dst)

        print('subway:', path_subway)

    def test_bike_metro(self):
        ecosystem = Ecosystem("http://team09.xp65.renault-digital.com", "env")
        first_path = shortestpath.get_shortest_paths({"x": 15.8, "y": 5.6}, {"x": 18.2, "y": 3.8}, "metro", "http://team09.xp65.renault-digital.com")
        print(first_path)
        second_path = shortestpath.subway_bike_path({"x": 15.8, "y": 5.6}, {"x": 18.2, "y": 3.8}, ecosystem)
        print(second_path)



if __name__ == '__main__':
    unittest.main()
