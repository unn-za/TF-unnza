import r2r_dac as r2r
import signal_generator as sg
import time
import RPi.GPIO as gp
gp.setmode(gp.BCM)
amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000
if __name__ == "__main__":
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
    while True:
        try:
            sg.wait_for_sampling_period(sampling_frequency)
            dac.set_voltage(amplitude*sg.get_sin_wave_amplitude(signal_frequency, time.time()))
        finally:
            pass 
