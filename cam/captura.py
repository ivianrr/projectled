import RPi.GPIO as GPIO       
import time
from picamera import PiCamera



def toggle(filtro=None):
    global IR
    if filtro=="IR":
        IR=True
    elif filtro=="DIA":
        IR=False
    else:
        IR=not IR        
    GPIO.output(port_or_pin, int(not IR))  
    print("Modo"+("IR" if IR else "DAY"))


port_or_pin = 40
GPIO.setmode(GPIO.BCM)    
GPIO.setup(port_or_pin, GPIO.OUT)


camera = PiCamera()
camera.rotation = 180
time.sleep(2)
IR=True
print('setup')


toggle("IR")
camera.start_preview()
camera.start_recording('/home/pi/Desktop/video.h264')
time.sleep(5)
camera.stop_recording()
camera.stop_preview()

camera.close()
GPIO.cleanup()
