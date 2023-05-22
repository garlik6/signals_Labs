import csv
import numpy as np

amplitude = 0.2
frequency = 13427.73438
phaseDeg = 10
phase = np.deg2rad(phaseDeg)
sampling_freq = 100000
duration = 0.1
offset = 0.5

print(phase)
targetTime = 0.001

teorethicalValue = offset + amplitude * np.cos(2 * np.pi * frequency * targetTime + phase)

with open('cosine_signal.csv', 'r') as f:
    reader = csv.reader(f)
    row1 = next(reader)
    duration = float(row1[0])
    sampling_freq = float(row1[1])
    signal = np.genfromtxt(f)

print(signal[0])

print(targetTime * sampling_freq)

csvValue = signal[int(targetTime * sampling_freq)]

print(teorethicalValue)
print(csvValue)

norm = np.linalg.norm(signal)
print("Норма встроенная функция", norm)

norm = 0
for s in signal:
    norm += s ** 2
norm = np.sqrt(norm)

print("Норма самостоятельный расчет", norm)

energy = np.sum(np.square(signal))
print("Энергия", energy)
print("Корень из энергии", np.sqrt(energy))
