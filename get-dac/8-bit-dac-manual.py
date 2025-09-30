import RPi.GPIO as gp
#import time 
gp.setmode(gp.BCM)
leds = [16, 20, 21, 25, 26, 17, 27, 22]
gp.setup(leds, gp.OUT)
gp.output(leds, 0)
dynamic_range = 3.18
def voltage2number(voltage):
    if not(0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 ; {dynamic_range} B)")
        print("Устанавливаем 0.0 В")
        return 0
    return int(voltage / dynamic_range*255)
def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
def number2dac(number):
    gp.output(leds, dec2bin(number))
try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage2number(voltage)
            number2dac(number)
        except ValueError:
            print("Вы ввели не число. Попробуйтe еще раз \n")
finally:
    gp.output(leds, 0)
    gp.cleanup()