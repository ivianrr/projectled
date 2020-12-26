from gpiozero import Button
from time import sleep

button = Button(18)

while True:
    if button.is_pressed:
        print("Silencio")
    else:
        print("Movimiento")
    sleep(1)
