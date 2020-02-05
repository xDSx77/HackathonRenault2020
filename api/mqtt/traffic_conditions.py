from mqtt_base import *


def traffic_conditions(roads: list, slowing_factors: list):
    # roads must be an array with the different road segments id
    # slowing_factors must be an array with the different slowing factors (1 to 10) corresponding to the roads
    # roads and slowing_factors must have the same size
    if len(roads) != len(slowing_factors):
        exit("The 2 arrays does not have the same size: " + str(len(roads)) + " != " + str(len(slowing_factors)))
    for i in range(len(slowing_factors)):
        if slowing_factors[i] < 1 or slowing_factors[i] > 10:
            exit("Incorrect value in slowing factors at index " + str(i) + ": " + str(slowing_factors[i]))

    traffic_payload = "["
    for i in range(len(roads)):
        if i < len(roads) - 1:
            traffic_payload += "{\"road\": \"" + str(roads[i]) + "\", " + "\"slowing_factor\": " + str(slowing_factors[i]) + "},"
        else:
            traffic_payload += "{\"road\": \"" + str(roads[i]) + "\", " + "\"slowing_factor\": " + str(slowing_factors[i]) + "}"
    traffic_payload += "]"
    print(traffic_payload)
    # client.subscribe(ENV + "/prod/user/situation", qos=0)
    client.publish(ENV + "/prod/city/morph/traffic_conditions", traffic_payload, qos=0, retain=False)
    # client.disconnect()