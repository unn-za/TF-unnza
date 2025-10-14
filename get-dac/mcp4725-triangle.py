import mcp4725_driver as mc
import signal_generator as sg
import time
amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000
if __name__ == "__main__":
    dac = mc.MCP4725(5.11, 0x61, True)
    while True:
        try:
            sg.wait_for_sampling_period(sampling_frequency)
            dac.set_voltage(amplitude*sg.get_trian_wave_amplitude(signal_frequency, time.time()))
        finally:
            pass 