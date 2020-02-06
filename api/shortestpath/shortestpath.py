import sys
sys.path.insert(1, '../rest/')

from ecosystem_api import Ecosystem
from path import Path

def get_available_cars(ecosystem: Ecosystem):
    vehicles = []
    cars = ecosystem.get_all_vehicles_info()
    for car in cars:
        if car["available"]:
            vehicles.append({"id": car["id"], "x": car["attitude"]["position"]["x"], "y": car["attitude"]["position"]["y"]})
    return vehicles

def set_best_car(car_paths: dict):
    """
    Transform car paths dict to only keep the best car
    """
    best_car = []
    min = 0.0
    for car in car_paths["cars"]:
        if len(best_car) == 0 or car['path_length'] < min:
            best_car = [car]
    car_paths["cars"] = best_car

def get_subway_path(eco, src: dict, dst: dict) -> list:

    # Get path between src to dst
    subway_path = eco.get_shortest_path_metro(src, dst)
    if subway_path == {}:
        return []

    subway_path['cars'][0]['costs'] = [float(elt) for elt in subway_path['cars'][0]['costs']]
    # subway_path['cars'][0]['costs'] = list(set(subway_path['cars'][0]['costs']))

    list_sub_path = []
    last_path = None

    # If first station not in src -> add a path of walk to first station
    first_station = subway_path['cars'][0]['paths'][1]
    if src['x'] != first_station[0] or src['y'] == first_station[1]:

        walk_path = eco.get_shortest_path_walk(src, {'x': first_station[0], 'y': first_station[1]})
        if walk_path == {}:
            return []

        if float(walk_path['cars'][0]['path_length']) != 0:
            walk_path['cars'][0]['costs'] = [ float(elt) for elt in walk_path['cars'][0]['costs']]
            # walk_path['cars'][0]['costs'] = list(set(walk_path['cars'][0]['costs']))
            list_sub_path.append(walk_path)

    # If last station not in dst -> add a path of walk to dst
    last_station = subway_path['cars'][0]['paths'][-1]

    if dst['x'] != last_station[0] or dst['y'] != last_station[1]:
        last_path = eco.get_shortest_path_walk({'x': last_station[0], 'y': last_station[1]}, dst)
        if last_path == []:
            return []
        if float(last_path['cars'][0]['path_length']) == 0:
            last_path = None

        last_path['cars'][0]['costs'] = [float(elt) for elt in last_path['cars'][0]['costs']]
        # last_path['cars'][0]['costs'] = list(set(last_path['cars'][0]['costs'][1:]))

    list_sub_path.append(subway_path)
    if last_path:
        list_sub_path.append(last_path)

    total_cost = 0
    for elt in list_sub_path:
        total_cost += float(elt['cars'][0]['path_length'])

    return Path(src, dst, list_sub_path, total_cost)


def get_shortest_paths(src: dict, dst: dict, filters: list, url: str):
    ecosystem = Ecosystem(url, "env")

    dict_filters = {
        "walk": ecosystem.get_shortest_path_walk,
        "metro": get_subway_path,
        "bike": ecosystem.get_shortest_path_bike,
        "car": ecosystem.get_shortest_path_car
    }

    shorter_paths = {}
    for key, function in dict_filters.items():

        if len(filters) == 0 or key in filters:
            if key == "car":
                available_cars = get_available_cars(ecosystem)

                if len(available_cars) != 0:
                    car_paths = function(src, dst, available_cars)
                    if car_paths != {}:

                        set_best_car(car_paths)
                        total_cost = float(car_paths['cars'][0]['path_length'])

                        shorter_paths[key] = Path(src, dst, [car_paths], total_cost)

            elif key == "metro":

                tmp_dict_path = function(ecosystem, src, dst)
                if tmp_dict_path != []:
                    shorter_paths[key] = tmp_dict_path
            else:

                tmp_dict_path = function(src, dst)
                if tmp_dict_path == {}:
                    continue
                total_cost = float(tmp_dict_path['cars'][0]['path_length'])
                tmp_path = Path(src, dst, [tmp_dict_path], total_cost)

                shorter_paths[key] = tmp_path


    return shorter_paths
