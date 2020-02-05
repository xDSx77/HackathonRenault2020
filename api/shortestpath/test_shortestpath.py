import unittest
import shortestpath

class MyTestCase(unittest.TestCase):
    def test_something(self):
        d = shortestpath.get_shortest_paths({"x": 15.8, "y": 5.6}, {"x": 18.2, "y": 3.8}, [], "http://team09.xp65.renault-digital.com")
        print(d)


if __name__ == '__main__':
    unittest.main()
