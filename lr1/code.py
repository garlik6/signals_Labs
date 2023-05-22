import numpy as np  # Внедрение зависимостей
import matplotlib.pyplot as plt
import csv

# Начальные данные
amplitude = 0.2
frequency = 13427.73438
phaseDeg = 10
phase = np.deg2rad(phaseDeg)
sampling_freq = 100000
duration = 0.1
offset = 0.5

# Подготовка значений по осям
t = np.arange(0, duration, 1/sampling_freq)
signal = offset + amplitude * np.cos(2*np.pi*frequency*t + phase)

# Запись в файл
with open('cosine_signal.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow([duration, sampling_freq])
    np.savetxt(f, signal, delimiter=",")

# Чтение из файла
with open('cosine_signal.csv', 'r') as f:
    reader = csv.reader(f)
    row1 = next(reader)
    duration = float(row1[0])
    sampling_freq = float(row1[1])
    signal = np.genfromtxt(f)

# Графики
t = np.arange(0, duration, 1/sampling_freq)
plt.plot(t, signal)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (V)")
plt.title("cosine_signal")
plt.show()
plt.plot(t[:int(t.size * 0.1)], signal[:int(signal.size * 0.1)])
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (V)")
plt.title("cosine_signal_10%")
plt.show()
plt.plot(t[:int(t.size * 0.01)], signal[:int(signal.size * 0.01)])
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (V)")
plt.title("cosine_signal_1%")
plt.show()

# Расчёт среднего значения
print("Среднее значение сигнала:")
print(np.mean(signal))
