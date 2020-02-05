from mqtt_base import *

def change_polution(air):
    # weather must be "normal", "pollution peak"
    payload = "{" + \
                "\"condition\": " + \
                "\""+ str(air) + "\"" + \
               "}"
    print(payload)
    # client.subscribe(ENV + "/prod/user/situation", qos=0)
    client.publish(ENV + "/prod/context/change/air", payload, qos=0, retain=False)

