import RPi.GPIO as gp
gp.setmode(gp.BCM)
led = 26
gp.setup(led, gp.OUT)
ph_transistor = 6
gp.setup(ph_transistor, gp.IN)
while True:
    gp.output(led, gp.input(ph_transistor))

