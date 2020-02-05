from flask import Flask
app = Flask(__name__)


@app.route("/api/subscribe_mission")
# Subscribe to the mission channel
def subscribe_mission():
    import mqtt_base

    mqtt_base.client.subscribe(mqtt_base.ENV + "/prod/user/mission", qos=0)
    mqtt_base.client.loop_forever()


subscribe_mission()
