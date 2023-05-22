import csv
import numpy as np

# чтение из файлов
with open('02_sn.csv', 'r') as f:
    reader = csv.reader(f)
    row1 = next(reader)
    sampling_freq = float(row1[1])
    mixture = np.genfromtxt(f)

fftSamples = 10000

# Расчет спектров с помощью БПФ
mixture_fft = np.abs(np.fft.rfft(mixture, fftSamples)) / (fftSamples / 2)
signalArg = np.argmax(mixture_fft)

# Рассмотрим разное колличество осчетов, которое может прибавляться к энергии сигнала
print("index of signal =")
for radius in range(10):
    power_of_signal = 0
    for i in range (signalArg - radius, signalArg + radius + 1):
        power_of_signal += mixture_fft[i] ** 2
    power_of_noise = np.trapz(mixture_fft**2) - power_of_signal
    snr_db = 10 * np.log10(power_of_signal / power_of_noise)
    print("SNR для отсчетов [%d-%d] = %f" %(signalArg - radius, signalArg + radius, snr_db))
