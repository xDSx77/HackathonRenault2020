import paho.mqtt.client as mqtt
import logging
import json

logging.basicConfig(level=logging.DEBUG)
with open("../config.dev.json") as json_f:
    json_data = json.load(json_f)

ENV = json_data['environment']


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


# The callback for when a client subscribe to a MQTT channel
def on_subscribe(client, userdata, mid, granted_qos):
    print(userdata)


# Create the client
client = mqtt.Client()

# Set the callback functions
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe

# Set the credentials for the connection
client.username_pw_set(json_data['broker_username'], json_data['broker_password'])

# Initialize the connection
client.connect(json_data['broker_domain'], port=json_data['broker_port'], keepalive=60)