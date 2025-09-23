import RPi.GPIO as gp
import time
gp.setmode(gp.BCM)
leds = [16, 12, 25, 17, 27, 23, 22, 24]
gp.setup(leds, gp.OUT)
gp.output(leds, 0)
up = 9
down = 10
gp.setup(up, gp.IN)
gp.setup(down, gp.IN)
num = 0
def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
sleep_time = 0.2
while True:
    if(gp.input(up) and gp.input(down)):
        num = 255
    else:
        if gp.input(up):
            num = num + 1
            if(num > 255):
                num = 0
            print(num, dec2bin(num))
            time.sleep(sleep_time)
        if gp.input(down):
            num = num - 1
            if(num < 0):
                num = 0
            print(num, dec2bin(num))
            time.sleep(sleep_time)
    gp.output(leds, dec2bin(num))
    time.sleep(sleep_time)
