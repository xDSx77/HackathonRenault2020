from mqtt_base import MqttBase


# Subscribe to the mission channel
def subscribe_mission():

    mqtt_base = MqttBase()
    mqtt_base.client.subscribe(mqtt_base.env + "/prod/user/mission", qos=0)
    # mqtt_base.client.loop_forever()


