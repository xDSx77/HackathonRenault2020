from mqtt_base import *


# Stop the agent while moving
def stop_agent():
    # client.subscribe(ENV + "/prod/user/status", qos=0)
    client.publish(ENV + "/prod/user/stop", None, qos=0, retain=False)
    # client.disconnect()
