from machine import Pin
import dht
import time

dht_sensor = dht.DHT11(Pin(14))

while True:
    try:
        dht_sensor.measure() #Takes new readings of temperature and humidity
        temperature = dht_sensor.temperature() #in Celsius
        humidity = dht_sensor.humidity() #in %
        print("1")

        print("Temperature:", temperature, "°C")
        print("Humidity:", humidity, "%")

    except OSError as e:
        print("Sensor read error:", e)
    time.sleep(2)