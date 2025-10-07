import RPi.GPIO as gp

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        gp.setmode(gp.BCM)
        gp.setup(self.gpio_pin, gp.OUT, initial = 0)
        self.pwm = gp.PWM(self.gpio_pin, self.pwm_frequency)
        self.pwm.start(0.0)
    def deinit(self):
        gp.output(self.gpio_pin, 0)
        gp.cleanup()

    def set_voltage(self, voltage):
        if(voltage < 0.0 or voltage > self.dynamic_range):
            voltage = 0.0
        
        duty = (voltage / self.dynamic_range) * 100
        self.pwm.ChangeDutyCycle(duty)

if __name__ == "__main__":
    dac = PWM_DAC(12, 500, 3.290, True)
    try:
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()
