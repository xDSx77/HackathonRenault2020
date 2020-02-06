from mqtt_base import MqttBase


def change_weather(weather):
    # weather must be "snow", "rain", "normal", "heat wave"
    payload = "{" + \
                "\"condition\": " + \
                "\""+ str(weather) + "\"" + \
               "}"
    print(payload)
    mqtt_base = MqttBase()
    # mqtt_base.client.subscribe(mqtt_base.env + "/prod/user/situation", qos=0)
    mqtt_base.client.publish(mqtt_base.env + "/prod/context/change/weather", payload, qos=0, retain=False)
