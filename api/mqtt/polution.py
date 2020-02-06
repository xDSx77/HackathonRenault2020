from mqtt_base import MqttBase


def change_polution(air):
    # weather must be "normal", "pollution peak"
    payload = "{" + \
                "\"condition\": " + \
                "\""+ str(air) + "\"" + \
               "}"
    print(payload)
    mqtt_base = MqttBase()
    # mqtt_base.client.subscribe(mqtt_base.env + "/prod/user/situation", qos=0)
    mqtt_base.client.publish(mqtt_base.env + "/prod/context/change/air", payload, qos=0, retain=False)

