from machine import ADC, Pin
from time import sleep

class Light:
    def __init__(self, pin=28):
        self.ldr = ADC(Pin(pin))

    def adc_to_lux(self, adc_val):
        # These should be your calibration values
        adc_dark = 49000    # ADC reading at known low lux
        lumen_dark = 0.95        # Lumen at adc_dark

        adc_bright = 62500  # ADC reading at known bright level
        lumen_bright = 1   # Lumen at adc_bright

        # Slope of linear interpolation 
        m = (lumen_bright - lumen_dark) / (adc_bright - adc_dark)
        b = lumen_dark - m * adc_dark

        lumen = m * adc_val + b

        if lumen < 0:
            lumen = 0

        return lumen

    def readLux(self):
        adc_value = self.ldr.read_u16()
        lux = self.adc_to_lux(adc_value)
        return f"{lux:.2f}"

