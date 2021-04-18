from adafruit_circuitplayground import cp
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    if rc == 0:
        cp.red_led = True
        client.subscribe("cpx-switch/#") #through the hashtag sign, it reads all the topic

def on_message(client, userdata, msg):
    # print(msg.topic+" "+msg.payload.decode())
    if msg.topic == "cpx-switch/one": #if the msg.topic is equal to the topic cpx-switch/one

        if msg.payload.decode() == "true": #if msg.payload.decode() equals to true
            cp.pixels[0] = (255, 255, 255) #cp.pixels turn the lights
        else:
            cp.pixels[0] = (0, 0, 0)   #if not, the pixels will never turns on

    elif msg.topic == "cpx-switch/two":  #same process with switch one
        if msg.payload.decode() == "true":
            cp.pixels[1] = (255, 255, 255)
        else:
            cp.pixels[1] = (0, 0, 0)
    elif msg.topic == "cpx-switch/three": #same process with switch one
        if msg.payload.decode() == "true":
            cp.pixels[2] = (255, 255, 255)
        else:
            cp.pixels[2] = (0, 0, 0)

                                             #if all the topic is equal to true, index 0-2 will turn on the lights
cp.red_led = False

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

client.loop_forever()
