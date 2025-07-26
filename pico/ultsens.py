from machine import Pin, time_pulse_us
import time

TRIG_Pin = Pin(3, Pin.OUT)
ECHO_Pin = Pin(2, Pin.IN)

def get_distance():
    #Send 10us pulses
    TRIG_Pin.value(1)
    time.sleep_us(10)
    TRIG_Pin.value(0)

    #Measures how long echo is high (Echo goes high for the time it takes the sound to travel to object and back)
    duration = time_pulse_us(ECHO_Pin, 1, 30000)

    #Calculate distance (speed of sound = 0.0343 cm/s)
    distance = (duration / 2) * 0.0343 # in cm/us
    return distance

#Main loop
while True:
    dist = get_distance()
    print("Distance: {:.2f} cm".format(dist))
    time.sleep(0.5)