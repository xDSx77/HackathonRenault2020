from mqtt_base import *


# Set the state (open or close) for some subway lines
def subway_lines(lines: list, states: list):
    # lines must be an array with the different subway segments id
    # states must be an array with the states "open" or "close" corresponding to the line that must be changed
    # lines and states must have the same size
    if len(lines) != len(states):
        print("The 2 arrays does not have the same size: " + str(len(lines)) + " != " + str(len(states)))
        return
    for i in range(len(states)):
        if states[i] != "open" and states[i] != "close":
            print("Incorrect value in states at index " + str(i) + ": " + str(states[i]))
            return

    line_payload = "["
    for i in range(len(lines)):
        if i < len(lines) - 1:
            line_payload += "{\"line\": \"" + str(lines[i]) + "\", " + "\"state\": \"" + str(states[i]) + "\"},"
        else:
            line_payload += "{\"line\": \"" + str(lines[i]) + "\", " + "\"state\": \"" + str(states[i]) + "\"}"
    line_payload += "]"
    print(line_payload)
    mqtt_base = MqttBase()
    # mqtt_base.client.subscribe(mqtt_base.env + "/prod/environment/change/lines_state", qos=0)
    mqtt_base.client.publish(mqtt_base.env + "/prod/city/morph/lines_state", line_payload, qos=0, retain=False)
    # mqtt_base.client.disconnect()
