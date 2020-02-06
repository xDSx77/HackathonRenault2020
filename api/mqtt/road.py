from mqtt_base import MqttBase


class Road:
    # road is the name of the road
    # state is the status of the road : "close" / "open"

    def __init__(self, abs, ord):
        self.road = abs
        self.state = ord


def change_road(car: list, bike: list, walk: list):
    # car, bike walk  must be a list of Road

    payload_car = "{ "+ \
                "\"car\": ["

    for i in range(len(car)):
        if i < len(car)-1:
            payload_car += "{\"road\": \"" + str(car[i].road) + "\", " + "\"state\": \"" + str(car[i].state) + "\"},"
        else:
            payload_car += "{\"road\": \"" + str(car[i].road) + "\", " + "\"state\": \"" + str(car[i].state) + "\"}"

    payload_car += "] "+ \
                   " },"

    payload_bike = "{ "+ \
                "\"bike\": ["
    for i in range(len(bike)):
        if i < len(bike)-1:
            payload_bike += "{\"road\": \"" + str(bike[i].road) + "\", " + "\"state\": \"" + str(bike[i].state) + "\"},"
        else:
            payload_bike += "{\"road\": \"" + str(bike[i].road) + "\", " + "\"state\": \"" + str(bike[i].state) + "\"}"

    payload_bike += "] "+ \
                   " },"

    payload_walk = "{ "+ \
                "\"walk\": ["
    for i in range(len(walk)):
        if i < len(walk)-1:
            payload_walk += "{\"road\": \"" + str(walk[i].road) + "\", " + "\"state\": \"" + str(walk[i].state) + "\"},"
        else:
            payload_walk += "{\"road\": \"" + str(walk[i].road) + "\", " + "\"state\": \"" + str(walk[i].state) + "\"}"

    payload_walk += "] "+ \
                   " }"

    payload = "[" + payload_car + payload_bike + payload_walk + "]"
    print(payload)
    mqtt_base = MqttBase()
    mqtt_base.client.publish(mqtt_base.env + "/prod/city/morph/roads_status", payload, qos=0, retain=False)


