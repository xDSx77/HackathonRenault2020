import sys
sys.path.insert(1, '../rest/')

from ecosystem_api import Ecosystem

def get_shortest_paths(src: dict, dst: dict, filters: list, url: str):
    ecosystem = Ecosystem(url, "env")
    dict_filters = {"walk": ecosystem.get_shortest_path_walk,
                    "metro": ecosystem.get_shortest_path_metro,
                    "bike": ecosystem.get_shortest_path_bike,
                    "car": ecosystem.get_shortest_path_car}

    shorter_paths = {}
    for key, function in dict_filters.items():
        if len(filters) == 0 or key in filters:
            if key == "car":
                continue # TODO
            else:
                shorter_paths[key] = function(src, dst)
    return shorter_paths