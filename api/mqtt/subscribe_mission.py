from . import mqtt_base


# Subscribe to the mission channel
def subscribe_mission():

    mqtt = mqtt_base.MqttBase()
    mqtt.client.subscribe(mqtt.env + "/prod/user/mission", qos=0)
    while mqtt.data is None:
        mqtt.client.loop()
    print(mqtt.data)
    return mqtt.data


