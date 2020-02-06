import sys
import os
import json

from flask import Flask, request

app = Flask(__name__)

sys.path.insert(1, "../shortestpath")
import shortestpath

config_path = "../config.dev.json"


@app.route("/api/get/shortestpath", methods=['GET', 'POST'])
def get_shortest_paths() -> dict:
    """
    Get shortest path according to config file
    """
    filters = []  # TODO get filters
    src = {"x": 0, "y": 0} # TODO get dst and src
    dst = {"x": 0, "y": 0}
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
