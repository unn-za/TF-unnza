import matplotlib.pyplot as plt
def plot_voltage_vs_time(time, voltage, max_voltage: float, max_time: float):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    plt.title('График зависимости напряжения на входе АЦП от времени')
    plt.xlabel('Время, с')
    plt.ylabel('Напряжение, В')
    plt.xlim(0, max_time)
    plt.ylim(0, max_voltage)
    plt.grid(True)
    plt.show()

def plot_sampling_period_hist(sampling_periods, max_period):
    plt.figure(figsize=(10, 6))
    plt.hist(sampling_periods)
    plt.grid(True)
    plt.xlim(0, max_period)
    plt.xlabel("Период, с")
    plt.ylabel("Количество измерений")
    plt.title("Распределение периодов дескретизации измерений по времени на одно измерение")
    plt.show()