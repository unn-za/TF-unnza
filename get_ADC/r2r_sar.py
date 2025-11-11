import r2r_adc as r2
from adc_plot import plot_voltage_vs_time as plot, plot_sampling_period_hist as hist
import time

adc = r2.R2R_ADC(3.18, 0.001)
voltage_values = list()
time_values = list()
sampling_periods = list()
duration = 3.0
max_voltage = 3.183

if __name__ == "__main__":

    try:
        exp_start = time.time()
        while time.time() - exp_start <= duration:
            voltage_values.append(adc.get_sar_voltage())
            time_values.append(time.time() - exp_start)

        for i in range(1, len(time_values)):
            sampling_periods.append(time_values[i] - time_values[i-1])

        plot(time_values, voltage_values, max_voltage, duration)
        hist(sampling_periods, max(sampling_periods))  
    finally:
        adc.deinit()