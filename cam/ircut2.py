import RPi.GPIO as GPIO       
import time
from picamera import PiCamera




port_or_pin = 40
GPIO.setmode(GPIO.BCM)    
GPIO.setup(port_or_pin, GPIO.OUT)

time.sleep(2)
IR=True
print('setup')


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


camera = PiCamera()
camera.rotation = 180

camera.start_preview(alpha=200)
print("mostrando preview")
time.sleep(5)
toggle()
time.sleep(5)
toggle("IR")
time.sleep(5)
toggle("DIA")
time.sleep(5)
camera.stop_preview()
camera.close()
GPIO.cleanup()
