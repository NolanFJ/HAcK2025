from connections import connect_mqtt, connect_internet
from time import sleep
from Sensors.Light import Light
import random

lightSensor = Light(28)

# mainly just testing connection
def cb(topic, msg):
    if topic == b"take_picture":
        print(msg.decode())

def main():
    try:
        connect_internet("", password="")
        client = connect_mqtt("", "", "")
        
        client.set_callback(cb)
        client.subscribe(b"take_picture")
        
        print("Subscribed to take_picture topic")
        
        counter = 0
        # main loop to check sensor data
        while True:
            client.check_msg()
            
            if (counter % 20):
                brightness = lightSensor.readBrightness()
                client.publish("light", str(brightness))
                print(f"Light brightness: {brightness}%")
            
            counter += 1
            sleep(0.1)
            
    except KeyboardInterrupt:
        print('keyboard interrupt')
        
if __name__ == "__main__":
    main()

