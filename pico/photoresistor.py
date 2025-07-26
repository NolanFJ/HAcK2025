from machine import ADC, Pin
import time

class Light:
    def __init__(self, pin=28):
        self.ldr = ADC(Pin(pin))
        
    #Function to convert raw ADC to voltage
    def adcToVoltage(self, raw):
        return (raw / 65535) * 3.3
    
    def readBrightness(self):
        rawValue = self.ldr.read_u16() # 16-bit reading
        voltage = self.adcToVoltage(rawValue)
        
        brightness = (rawValue / 65535) * 100
        
        return (round(brightness, 1))
