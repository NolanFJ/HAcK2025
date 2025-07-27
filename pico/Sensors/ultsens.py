from machine import Pin, time_pulse_us
import time

class Ultrasonic:
    def __init__(self):
        self.trig_pin = Pin(3, Pin.OUT) # Trig pin at GPIO 3
        self.echo_pin = Pin(2, Pin.IN) # Echo pin at GPIO 2
    
    # Read distance from ultrasonic sensor in cm
    def readDistance(self):
        # Send 10us pulse
        self.trig_pin.value(1)
        time.sleep_us(10)
        self.trig_pin.value(0)

        # Measure how long echo is high (Echo goes high for the time it takes the sound to travel to object and back)
        try:
            duration = time_pulse_us(self.echo_pin, 1, 30000)
            
            # Calculate distance (speed of sound = 0.0343 cm/us)
            distance = (duration / 2) * 0.0343  # in cm
            return round(distance, 2)
            
        except OSError:
            # Return -1 if timeout or no echo received
            return -1

