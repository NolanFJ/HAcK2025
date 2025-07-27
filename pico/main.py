from connections import connect_mqtt, connect_internet
from time import sleep
from Sensors.Light import Light
from Sensors.temp import TempHumid
from Sensors.ultsens import Ultrasonic
import random
from machine import Pin, I2C
import ssd1306

lightSensor = Light(28)
tempSensor = TempHumid(4)
ultraSensor = Ultrasonic(3, 2)

i2c = I2C(0, sda=Pin(0), scl=Pin(1))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# mainly just testing connection
def cb(topic, msg):
    if topic == b"take_picture":
        print(msg.decode())

# receive a message and display to OLED
def message(topic, msg):
    if topic == b"display":
        # Clear the display by filling it with white and then showing the update
        oled.fill(1)
        oled.show()
        sleep(1)  # Wait for 1 second

        # Clear the display again by filling it with black
        oled.fill(0)
        oled.show()
        sleep(1)  # Wait for another second

        text = msg.decode()  # Convert bytes to string
        oled.text(text, 0, 0)  # Display decoded message at position (0, 0)
        #oled.text('different hello', 0, 16)  # Display "sunfounder.com" at position (0, 16)

        # The following line sends what to show to the display
        oled.show()
        print(msg.decode())


def main():
    try:
        connect_internet("", password="")
        client = connect_mqtt("", "", "")
        
        client.set_callback(cb)
        client.subscribe(b"take_picture")
        
        client.set_callback(message)
        client.subscribe(b"display")
        
        print("Subscribed to take_picture topic")
        print("Subscribed to display topic")
        
        counter = 0
        # main loop to check sensor data
        while True:
            client.check_msg()
            
            if (counter % 20):
                # light
                lux = lightSensor.readLux()
                client.publish("light", str(lux))
                #print(f"{lux}")
                
                # temp 
                temp = tempSensor.readTemp()
                client.publish("temp", str(temp))
                #print(f"Temp: {temp}")
                
                # humidity
                humidity = tempSensor.readHumidity()
                client.publish("humidity", str(humidity))
                #print(f"Humidity: {humidity}")
                
                # ultrasonic
                distance = ultraSensor.readDistance()
                client.publish("ultrasonic", str(distance))
                #print(f"Distance: {distance}")
                
            counter += 1
            sleep(0.2)
            
    except KeyboardInterrupt:
        print('keyboard interrupt')
        
if __name__ == "__main__":
    main()



