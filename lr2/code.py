import numpy as np
import matplotlib.pyplot as plt
import csv
np.seterr(divide='ignore', invalid='ignore')
sampling_freq = 100000
duration = 0.1
# Задам зерно случайности
np.random.seed(12)
# Генерируем сигнал
num_samples = int(sampling_freq * duration)

signal = np.random.uniform(low=-1, high=1, size=num_samples)

t = np.arange(0, duration, 1/sampling_freq)

with open('signal.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow([duration, sampling_freq])
    np.savetxt(f, signal, delimiter=",")

# Чтение из файла
with open('signal.csv', 'r') as f:
    reader = csv.reader(f)
    row1 = next(reader)
    duration = float(row1[0])
    sampling_freq = float(row1[1])
    signal = np.genfromtxt(f)

# Графики
# plt.plot(t, signal)
# plt.xlabel("Time (s)")
# plt.ylabel("Amplitude (V)")
# plt.title("Uniform Noise Signal")
# plt.show()
# plt.plot(t[:int(t.size * 0.5)], signal[:int(signal.size * 0.5)])
# plt.xlabel("Time (s)")
# plt.ylabel("Amplitude (V)")
# plt.title("Uniform Noise Signal")
# plt.show()

# расчёт мат ожидания и дисперсии
mean = np.mean(signal)
variance = np.var(signal)
print("Mean: ", mean)
print("Variance: ", variance)

x = np.arange(100000)
var = np.zeros(100000)

for i in range(1, 100000):
    var[i] = np.var(signal[:i])

plt.plot(np.arange(7500), var[:7500])
plt.xlabel("Number of samples")
plt.ylabel("Variance")
plt.title("Uniform Noise Variance")
plt.show()
