from mqtt_base import *


# Reset the agent MeaooTime
def reset_agent():
    client.publish(ENV + "/prod/city/reset", None, qos=0, retain=False)
    # client.disconnect()
