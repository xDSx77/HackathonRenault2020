from mqtt_base import *


# Teleport the agent with the according vehicle type to a certain coordinate of the MeaooCity
def teleport_agent(vehicle_type: str, arrival_point: tuple):
    # vehicle_type must be "walk", "subway", "bike" or "car"
    # arrival_point must be a tuple like (10, 2.5)
    if vehicle_type != "walk" and vehicle_type != "subway" and vehicle_type != "bike" and vehicle_type != "car":
        print("Wrong vehicle type: " + vehicle_type)
        return
    if len(arrival_point) != 2:
        print("Not a correct tuple for the arrival point: " + str(arrival_point))
        return

    teleport_payload = "{" + \
                       "\"vehicle_type\": \"" + str(vehicle_type) + "\"," \
                       "\"path\": [" \
                       "    [" + str(arrival_point[0]) + ", " + str(arrival_point[1]) + "]," \
                       "    [" + str(arrival_point[0] + 0.1) + ", " + str(arrival_point[1]) + "]" \
                       "]," \
                       "\"costs\": [0.0, 0.0]" \
                       "}"
    print(teleport_payload)
    mqtt_base = MqttBase()
    # mqtt_base.client.subscribe(mqtt_base.env + "/prod/user/status", qos=0)
    mqtt_base.client.publish(mqtt_base.env + "/prod/user/path-to-target", teleport_payload, qos=0, retain=False)
    # mqtt_base.client.disconnect()
