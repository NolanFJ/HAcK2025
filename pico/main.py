from connections import connect_mqtt, connect_internet
from time import sleep
from Sensors.Light import Light
from Sensors.temp import TempHumid
from Sensors.ultsens import Ultrasonic
from machine import Pin, I2C
import ssd1306 #IMPORTANT NEED FOR OLED DISPLAY!

# Initialize sensors
lightSensor = Light(28)
tempSensor = TempHumid(4)
ultraSensor = Ultrasonic(3, 2)

# Initialize I2C and OLED (assumes I2C0 with SDA=GP0, SCL=GP1)
i2c = I2C(0, scl=Pin(1), sda=Pin(0))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Clear OLED on startup
oled.fill(0)
oled.text("Starting...", 0, 0)
oled.show()

def handle_message(topic, msg):
    if topic == b"take_picture":
        print("Picture message:", msg.decode())
    elif topic == b"display":
        display_text = msg.decode()
        print("OLED Display:", display_text)
        
        oled.fill(0)
        # Display up to 3 lines if message is long
        oled.text(display_text[0:16], 0, 0)
        if len(display_text) > 16:
            oled.text(display_text[16:32], 0, 10)
        if len(display_text) > 32:
            oled.text(display_text[32:48], 0, 20)
        oled.show()

def main():
    try:
        connect_internet("", password="")
        client = connect_mqtt("", "", "")
        
        client.set_callback(handle_message)
        client.subscribe(b"take_picture")
        client.subscribe(b"display")
        
        print("Subscribed to topics: take_picture, display")

        counter = 0
        while True:
            client.check_msg()
            
            # Publish sensor data every few cycles
            if counter % 20 == 0:
                lux = lightSensor.readLux()
                client.publish("light", str(lux))

                temp = tempSensor.readTemp()
                client.publish("temp", str(temp))

                humidity = tempSensor.readHumidity()
                client.publish("humidity", str(humidity))

                distance = ultraSensor.readDistance()
                client.publish("ultrasonic", str(distance))
         
            counter += 1
            sleep(0.2)

    except KeyboardInterrupt:
        print("Keyboard interrupt detected. Exiting...")

if __name__ == "__main__":
    main()
