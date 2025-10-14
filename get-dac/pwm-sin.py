import pwm_dac as pm
import signal_generator as sg
import time
amplitude = 3.2
signal_frequency = 10
sampling_frequency = 50
if __name__ == "__main__":
    dac = pm.PWM_DAC(12, 5000, 3.290, True)
    while True:
        try:
            sg.wait_for_sampling_period(sampling_frequency)
            dac.set_voltage(amplitude*sg.get_sin_wave_amplitude(signal_frequency, time.time()))
        finally:
            pass 