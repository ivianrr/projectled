from gpiozero import Buzzer, MotionSensor
from time import sleep

buzzer = Buzzer(22)
pir = MotionSensor(18)

def pitido(t):
	buzzer.on()
	sleep(t)
	buzzer.off()

while True:
	pir.wait_for_motion()
	print("Intruso!")
	pitido(.1)
	sleep(.15)
	pitido(.1)
	pir.wait_for_no_motion()

