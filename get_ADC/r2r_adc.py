import time
import RPi.GPIO as gp

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        gp.setmode(gp.BCM)
        gp.setup(self.gpio_bits, gp.OUT, initial = 0)

    def deinit(self):
        gp.output(self.gpio_bits, 0)
        gp.cleanup()
    def set_number(self, number):
        if (number < 0 or number >255):
            number = 0
        gp.output(self.gpio_bits, [int(element) for element in bin(number)[2:].zfill(8)])

    def set_voltage(self, voltage):
        self.set_number(int(voltage / self.dynamic_range*255))


class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21
        gp.setmode(gp.BCM)
        self.dac = R2R_DAC(self.bits_gpio, self.dynamic_range)
        gp.setup(self.bits_gpio, gp.OUT, initial = 0)
        gp.setup(self.comp_gpio, gp.IN)

    def deinit(self):
        gp.output(self.bits_gpio, 0)
        gp.cleanup()
    def sequential_counting_adc(self):
        self.dac.set_number(0)
        for lol in range (0, 255):
            comp = gp.input(self.comp_gpio)
            self.dac.set_number(lol)
            time.sleep(self.compare_time)
            if(comp == 1):
                return lol
        return 255

    def get_sc_voltage(self):
        return(self.sequential_counting_adc()/255*self.dynamic_range)

if __name__ == "__main__":
    adc = R2R_ADC(3.183, 0.01)
    try:
        while True:
            print(adc.get_sc_voltage())
    finally:
        adc.deinit()