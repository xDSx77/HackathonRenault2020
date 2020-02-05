import paho.mqtt.client as mqtt

BROKER_DOMAIN = "mr1dns3dpz5mjj.messaging.solace.cloud"
ENV = "team09"
USER = ENV
PASSWORD = "hf9twck3zc"


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

# Create the client
client = mqtt.Client()

# Set the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Set the credentials for the connection
client.username_pw_set(USER, PASSWORD)

# Initialize the connection
client.connect(BROKER_DOMAIN, port=1883, keepalive=60)
