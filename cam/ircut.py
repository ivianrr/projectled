import RPi.GPIO as GPIO       
import time
port_or_pin = 40
GPIO.setmode(GPIO.BCM)    
GPIO.setup(port_or_pin, GPIO.OUT)

def toggle(sleep_=None):
    GPIO.output(port_or_pin, 1)  
    print('ON')
    if sleep_ is not None:
        time.sleep(sleep_)
    GPIO.output(port_or_pin, 0) 
    print('OFF')

for i in range(0, 2):
    print('toggle')
    toggle(4)
GPIO.cleanup()
