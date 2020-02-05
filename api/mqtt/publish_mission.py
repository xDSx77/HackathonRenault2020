from mqtt_base import *


# Publish a new mission with the list of positions that the agent must use
def publish_mission(message: str, positions: list):
    # message must be a string containing the presentation of the mission
    # positions must contains the list of tuple of the different coordinates where the agent must pass
    mission_payload = "{" + \
                      "\"mission\": \"" + message + "\"," + \
                      "\"positions\": ["
    for i in range(len(positions)):
        if len(positions[i]) != 2:
            print("Not a tuple at index " + str(i) + ": " + str(positions[i]))
            return
        if i < len(positions) - 1:
            mission_payload += "{" + \
                               "\"x\": " + positions[i][0] + "," + \
                               "\"y\": " + positions[i][1] + \
                               "},"
        else:
            mission_payload += "{" + \
                               "\"x\": " + positions[i][0] + "," + \
                               "\"y\": " + positions[i][1] + \
                               "}"
    mission_payload += "    ]" + \
                       "}"

    client.publish(ENV + "/prod/user/mission", mission_payload, qos=0, retain=False)
    # client.disconnect()
