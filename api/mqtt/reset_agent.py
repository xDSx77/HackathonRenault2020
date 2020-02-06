from mqtt_base import MqttBase


# Reset the agent MeaooTime
def reset_agent():
    mqtt_base = MqttBase()
    mqtt_base.client.publish(mqtt_base.env + "/prod/city/reset", None, qos=0, retain=False)
    # mqtt_base.client.disconnect()
