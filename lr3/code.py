import numpy as np
# import matplotlib.pyplot as plt
import csv

sampling_freq = 100000
duration = 0.1
aNoise = 0.17825018762674913

# Чтение из файла
with open('02_signal.csv', 'r') as f:
    reader = csv.reader(f)
    row1 = next(reader)
    duration = float(row1[0])
    sampling_freq = float(row1[1])
    noise = np.genfromtxt(f)


with open('cosine_signal.csv', 'r') as f:
    reader = csv.reader(f)
    row1 = next(reader)
    duration = float(row1[0])
    sampling_freq = float(row1[1])
    signal = np.genfromtxt(f)

signal = signal - np.mean(signal)
noise = noise * aNoise

mixture = signal + noise

with open('02_sn.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow([duration, sampling_freq])
    np.savetxt(f, mixture, delimiter=",")

t = np.arange(0, duration, 1/sampling_freq)

# plt.plot(t, mixture)
# plt.xlabel("time, s")
# plt.ylabel("signal + noise, V")
# plt.title("mixture of noise and signal")
# plt.show()
#
# plt.plot(t[:int(duration * sampling_freq * 0.05)], mixture[:int(duration * sampling_freq * 0.05)])
# plt.xlabel("time, s")
# plt.ylabel("signal + noise, V")
# plt.title(" 5% mixture of noise and signal")
# plt.show()


sigNorm = np.linalg.norm(signal)
noiseNorm = np.linalg.norm(noise)
dot = np.dot(signal, noise)
angle = np.arccos(dot /( sigNorm * noiseNorm))
print(np.rad2deg(angle))
