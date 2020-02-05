from mqtt_base import *


def teleport_agent(vehicle_type: str, arrival_point: tuple):
    # vehicle_type must be "walk", "subway", "bike" or "car"
    # arrival_point must be a tuple like (10, 2.5)
    if vehicle_type != "walk" and vehicle_type != "subway" and vehicle_type != "bike" and vehicle_type != "car":
        exit("Wrong vehicle type: " + vehicle_type)
    if len(arrival_point) != 2:
        exit("Not a correct tuple for the arrival point: " + str(arrival_point))

    teleport_payload = "{" + \
                       "\"vehicle_type\": \"" + str(vehicle_type) + "\"," \
                       "\"path\": [" \
                       "    [" + str(arrival_point[0]) + ", " + str(arrival_point[1]) + "]," \
                       "    [" + str(arrival_point[0] + 0.1) + ", " + str(arrival_point[1]) + "]" \
                       "]," \
                       "\"costs\": [0.0, 0.0]" \
                       "}"
    print(teleport_payload)
    # client.subscribe(ENV + "/prod/user/situation", qos=0)
    client.publish(ENV + "/prod/user/path-to-target", teleport_payload, qos=0, retain=False)
    # client.disconnect()