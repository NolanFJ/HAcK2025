from machine import Pin
import dht
import time

class TempHumid:
    def __init__(self, pin=4):
        self.dht_sensor = dht.DHT11(Pin(pin))
        
    def readTemp(self):
        try:
            self.dht_sensor.measure() #Takes new readings of temperature and humidity
            temperature = self.dht_sensor.temperature() #in Celsius
            humidity = self.dht_sensor.humidity() #in %
            return(temperature)
        except OSError as e:
            return("Sensor read error:", e)
        
    def readHumidity(self):
        try:
            self.dht_sensor.measure()
            humidity = self.dht_sensor.humidity()
            return(humidity)
        except OSError as e:
            return("Sensor read error:", e)
            

