from machine import Pin
import dht
import time

class TempHumid:
    def __init__(self, pin=4):
        self.dht_sensor = dht.DHT11(Pin(pin))
        
    # PLEASE FIX & TEST THISSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
    def readTemp(self):
        try:
            self.dht_sensor.measure() #Takes new readings of temperature
            temp_c = self.dht_sensor.temperature()
            temp_f = ((temp_c * (9 / 5)) + 32) # convert to fahrenheit
            return temp_f
        except OSError as e:
            return("Sensor read error:", e)
        
    def readHumidity(self):
        try:
            self.dht_sensor.measure() #Takes new readings of humidity
            return self.dht_sensor.humidity()
        except OSError as e:
            return("Sensor read error:", e)


