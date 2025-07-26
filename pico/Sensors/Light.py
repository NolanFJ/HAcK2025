from machine import ADC, Pin
from time import sleep

class Light:
    def __init__(self, pin=28):
        self.ldr = ADC(Pin(pin))
        self.R_fixed = 1000 # ohms
        
    #Function to convert raw ADC to lux
    def adc_to_lux(self, adc_val):
        voltage = adc_val * 3.3 / 65535 # convert to actual voltage
        if voltage == 0:
            return 0 # avoid division by zero
        
        # Compute LDR resistance based on voltage divider formula
        ldr_resistance = self.R_fixed * (3.3 - voltage) / voltage
        
        # These constants are general and may need tuning for your specific LDR
        A = 500000 # depends on LDR
        B = 1.4 # depends on LDR
        
        lux = (A / ldr_resistance) ** (1 / B)
        return lux
        
    
    def readLux(self):
        raw = self.ldr.read_u16()
        lux = self.adc_to_lux(raw)
        
        return f"Lux: {lux:.2f}"


