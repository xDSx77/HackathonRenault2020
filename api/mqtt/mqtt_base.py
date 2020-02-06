import paho.mqtt.client as mqtt
import logging
import json


class MqttBase:
    json_data = None
    env = None
    client = None

    # The callback for when the client receives a CONNACK response from the server.
    @staticmethod
    def on_connect(userdata, flags, rc):
        print("Connected with result code " + str(rc))

    # The callback for when a PUBLISH message is received from the server.
    @staticmethod
    def on_message(client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))

    # The callback for when a client subscribe to a MQTT channel
    @staticmethod
    def on_subscribe(client, userdata, mid, granted_qos):
        print(userdata)

    def __init__(self):
        # Enable debug logging for mqtt
        logging.basicConfig(level=logging.DEBUG)

        # Create the client
        self.client = mqtt.Client()

        # Set the callback functions
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_subscribe = self.on_subscribe

        with open("../config.dev.json") as json_f:
            self.json_data = json.load(json_f)
            self.env = self.json_data['environment']

        # Set the credentials for the connection
        self.client.username_pw_set(self.json_data['broker_username'], self.json_data['broker_password'])

        # Initialize the connection
        self.client.connect(self.json_data['broker_domain'], port=self.json_data['broker_port'], keepalive=60)


