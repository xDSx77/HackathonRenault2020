from mqtt_base import MqttBase


# Move the agent with the according vehicle type to a coordinate of the MeaooCity
def move_agent(vehicle_type: str, target: tuple):
    # vehicle_type must be "walk", "subway", "bike" or "car"
    # target must be a tuple like (4, 5.7) corresponding to the target coordinates
    # lines and states must have the same size
    if vehicle_type != "walk" and vehicle_type != "subway" and vehicle_type != "bike" and vehicle_type != "car":
        print("Wrong vehicle type: " + vehicle_type)
        return
    if len(target) != 2:
        print("Not a correct tuple for the arrival point: " + str(target))
        return

    move_payload = "{" + \
                    "   \"vehicle_type\": \"" + str(vehicle_type) + "\"," \
                    "   \"target\": {\"x\": " + str(target[0]) + ", \"y\": " + str(target[1]) + "}" \
                    "}"
    # print(move_payload)
    mqtt_base = MqttBase()
    # mqtt_base.client.subscribe(mqtt_base.env + "/prod/user/status", qos=0)
    mqtt_base.client.publish(mqtt_base.env + "/prod/user/path", move_payload, qos=0, retain=False)
    # mqtt_base.client.disconnect()
