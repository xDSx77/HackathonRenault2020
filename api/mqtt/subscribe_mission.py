from mqtt_base import MqttBase
from flask import Flask
app = Flask(__name__)


@app.route("/api/subscribe_mission")
# Subscribe to the mission channel
def subscribe_mission():

    mqtt_base = MqttBase()
    mqtt_base.client.subscribe(mqtt_base.env + "/prod/user/mission", qos=0)
    mqtt_base.client.loop_forever()


subscribe_mission()
