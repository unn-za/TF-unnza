import RPi.GPIO as gp
import time
gp.setmode(gp.BCM)
led = 26
button = 13
gp.setup(led, gp.OUT)
gp.setup(button, gp.IN)
state = 0
while True:
    if gp.input(button):
        state = not state
        gp.output(led, state)
        time.sleep(0.2)