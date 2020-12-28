from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview(alpha=220)
print("mostrando preview")
sleep(15)
camera.stop_preview()
camera.close()
