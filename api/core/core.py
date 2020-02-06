import sys
import os
from flask import Flask
import json

sys.path.insert(1, "../shortestpath")
import shortestpath

config_path = "../config.dev.json"


def set_config_path() -> bool:
    """
    Set config file path, return true if valid, false otherwise
    :param path:
    :return:
    """
    path = "" # TODO request
    if not os.path.isfile(path):
        return False

    config_path = path
    return True


def get_shortest_paths() -> dict:
    """
    Get shortest path according to config file
    """
    filters = "" # TODO request text
    src = {"x": 0, "y": 0} # TODO request text
    dst = {"x": 0, "y": 0} # TODO request text
    with open(config_path) as fp:
        data = json.load(fp)
        if "url" in data:
            url = data[""]
        else:
            print("URL IS NOT IN CONFIG FILE")
            return {}

    return shortestpath.get_shortest_paths(src, dst, filters, url)


def is_new_update() -> bool:
    """
    Check if the ecosystem was updated recently
    """
    return
