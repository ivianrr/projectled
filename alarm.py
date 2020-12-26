from gpiozero import Buzzer, MotionSensor
from time import sleep

buzzer = Buzzer(22)
pir = MotionSensor(18)

while True:
	pir.wait_for_motion()
	buzzer.on()
	print("Intruso!")
	sleep(1)
	buzzer.off()
	pir.wait_for_no_motion()

