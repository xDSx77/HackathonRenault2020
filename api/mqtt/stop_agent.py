from mqtt_base import MqttBase


# Stop the agent while moving
def stop_agent():
    mqtt_base = MqttBase()
    # mqtt_base.client.subscribe(mqtt_base.env + "/prod/user/status", qos=0)
    mqtt_base.client.publish(mqtt_base.env + "/prod/user/stop", None, qos=0, retain=False)
    # mqtt_base.client.disconnect()
