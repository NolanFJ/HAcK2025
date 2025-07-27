from machine import ADC, Pin
from time import sleep

# PLEASE FIX & TEST THISSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
class Light:
    def __init__(self, pin=28):
        self.ldr = ADC(Pin(pin))
        self.fixed_resistor = 1000 # ohms
        
    #Function to convert raw ADC to lux
    def adc_to_lux(self, adc_val):
        voltage = adc_val * 3.3 / 65535 # convert to actual voltage
       
        # Don't think this is needed
        if voltage == 0:
            return 0 # avoid division by zero
        
        # Compute LDR resistance based on voltage divider formula
        ldr_resistance = self.fixed_resistor * (3.3 - voltage) / voltage

        # Need to adjust A and B . . . should only return lux
        A = 500000 # depends on LDR
        B = 1.4 # depends on LDR
        
        lux = (A / ldr_resistance) ** (1 / B)
        return ((lux / 100) + 0.05) # Calibrate
        
    def readLux(self):
        raw = self.ldr.read_u16()
        lux = self.adc_to_lux(raw)
        
        return f"Lux: {lux:.2f}"



