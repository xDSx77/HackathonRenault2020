import unittest
import shortestpath

from ecosystem_api import Ecosystem

class MyTestCase(unittest.TestCase):
    def test_something(self):
        d = shortestpath.get_shortest_paths({"x": 15.8, "y": 5.6}, {"x": 18.2, "y": 3.8}, [], "http://team09.xp65.renault-digital.com")
        print(d)

    def test_with_print(self):
        d = shortestpath.get_shortest_paths({ "x":17.79, "y":2.0 }, { "x":18.0, "y":2.0 }, [], "http://team09.xp65.renault-digital.com")
        for k, v in d.items():
            print(k, v)

    def test_metro(self):
        ecosystem = Ecosystem("http://team09.xp65.renault-digital.com", "env")

        src = { "x":17.79, "y":2.0 }
        dst = { "x":18.0, "y":2.0 }

        path_subway = ecosystem.get_shortest_path_metro(src, dst)

        print('subway:', path_subway)




if __name__ == '__main__':
    unittest.main()
