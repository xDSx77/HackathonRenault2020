import sys
sys.path.insert(1, '../rest/')

from ecosystem_api import Ecosystem
from path import Path

def get_available_cars(ecosystem: Ecosystem):
    vehicles = []
    cars = ecosystem.get_all_vehicles_info()
    for car in cars:
        if car["available"]:
            vehicles.append({"id": car["attitude"]["id"], "x": car["attitude"]["position"]["x"], "y": car["attitude"]["position"]["y"]})
    return vehicles


def get_subway_path(eco, src: dict, dst: dict) -> list:

    # Get path between src to dst
    subway_path = eco.get_shortest_path_metro(src, dst)
    if subway_path == {}:
        print('src:', src, ' dest:', dst)
        print('here:', subway_path)
        return []

    list_sub_path = []
    last_path = None

    # If first station not in src -> add a path of walk to first station
    first_station = subway_path['cars'][0]['paths'][1]
    if src['x'] != first_station[0] or src['y'] == first_station[1]:

        walk_path = eco.get_shortest_paths_walk(src, {'x': first_station[0], 'y': first_station[1]})
        if walk_path == {}:
            return []

        list_sub_path.append(walk_path)

    # If last station not in dst -> add a path of walk to dst
    last_station = subway_path['cars'][0]['paths'][-1]
    if dst['x'] != last_station[0] or dst['y'] != last_station[1]:
        last_path = eco.get_shortest_paths({'x': last_station[0], 'y': last_station[1]}, dst)

    subway_path['paths'] = subway_path['paths'][1:]
    subway_path['cost'] = subway_path['cost'][1:]
    list_sub_path.append(subway_path)

    if last_path:
        list_sub_path.append(last_path)


    total_cost = 0
    for elt in list_sub_path:
        total_cost += float(elt['cars'][0]['path_lenght'])

    return Path(src, dst, list_sub_path, total_cost)


def get_shortest_paths(src: dict, dst: dict, filters: list, url: str):
    ecosystem = Ecosystem(url, "env")
    dict_filters = {"walk": ecosystem.get_shortest_path_walk,
                    "metro": get_subway_path,
                    "bike": ecosystem.get_shortest_path_bike,
                    "car": ecosystem.get_shortest_path_car}

    shorter_paths = {}
    for key, function in dict_filters.items():

        print('KEY:', key)

        if len(filters) == 0 or key in filters:
            if key == "car":
                available_cars = get_available_cars(ecosystem)
                if len(available_cars) != 0:
                    shorter_paths[key] = function(src, dst, available_cars)
            elif key == "metro":
                shorter_paths[key] = function(ecosystem, src, dst)
            else:

                tmp_dic_path = function(src, dst)
                total_cost = float(tmp_dic_path['cars'][0]['path_length'])
                tmp_path = Path(src, dst, [tmp_dic_path], total_cost)

                shorter_paths[key] = tmp_path

    return shorter_paths
