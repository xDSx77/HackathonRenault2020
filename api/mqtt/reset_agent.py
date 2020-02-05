from mqtt_base import *


def reset_agent():
    client.publish(ENV + "/prod/city/reset", None, qos=0, retain=False)
    # client.disconnect()
