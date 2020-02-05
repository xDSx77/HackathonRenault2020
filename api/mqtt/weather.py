from mqtt_base import *

def change_weather(weather):
    # weather must be "snow", "rain", "normal", "heat wave"
    payload = "{" + \
                "\"condition\": " + \
                "\""+ str(weather) + "\"" + \
               "}"
    print(payload)
    # client.subscribe(ENV + "/prod/user/situation", qos=0)
    client.publish(ENV + "/prod/context/change/weather", payload, qos=0, retain=False)
