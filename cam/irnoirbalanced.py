import RPi.GPIO as GPIO       
from time import sleep
from picamera import PiCamera

port_or_pin = 40
def initfilter():
    GPIO.setmode(GPIO.BCM)    
    GPIO.setup(port_or_pin, GPIO.OUT)
    GPIO.output(port_or_pin, 0)  

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

initfilter()
sleep(.5)
camera = PiCamera(resolution=(1920, 1080), framerate=30) #(1280, 720)
camera.rotation = 180
# Set ISO to the desired value
camera.iso = 400
# Wait for the automatic gain control to settle
sleep(2)
# Now fix the values
camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g

# Finally, take several photos with the fixed settings
fldr="ims/"

toggle("IR")
sleep(0.3)
camera.capture(fldr+"imgIR.jpg")

toggle("DIA")
sleep(0.3)
camera.capture(fldr+"imgDIA.jpg")


camera.close()
GPIO.cleanup()
