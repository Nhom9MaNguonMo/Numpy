import numpy as np
import matplotlib.pyplot as plotter

# How many time points are needed, i.e., Sampling Frequency
samplingFrequency = 100
samplingInterval = 1 / samplingFrequency

# Begin and end time period of the signals
beginTime = 0
endTime = 10

# Frequencies of the signals
signal1Frequency = 4  # Lower than 7Hz (to be filtered)
signal2Frequency = 7  # 7Hz (should remain after filter)

# Time points
time = np.arange(beginTime, endTime, samplingInterval)

# Create two sine waves
amplitude1 = np.sin(2 * np.pi * signal1Frequency * time)
amplitude2 = np.sin(2 * np.pi * signal2Frequency * time)

# Sum of both sine waves
amplitude = amplitude1 + amplitude2

# Create subplot
figure, axis = plotter.subplots(4, 1)
plotter.subplots_adjust(hspace=1)

# Time domain representation for sine waves
axis[0].set_title('Sine wave with a frequency of 4 Hz')
axis[0].plot(time, amplitude1)
axis[0].set_xlabel('Time')
axis[0].set_ylabel('Amplitude')

axis[1].set_title('Sine wave with a frequency of 7 Hz')
axis[1].plot(time, amplitude2)
axis[1].set_xlabel('Time')
axis[1].set_ylabel('Amplitude')

# Combined sine wave (time domain)
axis[2].set_title('Sine wave with multiple frequencies (4 Hz + 7 Hz)')
axis[2].plot(time, amplitude1)
axis[2].set_xlabel('Time')
axis[2].set_ylabel('Amplitude')

# Frequency domain (Fourier Transform)
fourierTransform = np.fft.fft(amplitude) / len(amplitude)  # Normalize amplitude
frequencies = np.fft.fftfreq(len(amplitude), d=samplingInterval)

# High-pass filter: Remove frequencies below 7Hz
cutoff = 7
fourierTransform[np.abs(frequencies) < cutoff] = 0

# Inverse FFT to get filtered signal back in time domain
filtered_amplitude = np.fft.ifft(fourierTransform * len(amplitude))

# Plot frequency domain after applying filter
axis[3].set_title('Filtered Fourier transform (7Hz high-pass)')
axis[3].plot(frequencies[:len(frequencies)//2], np.abs(fourierTransform[:len(fourierTransform)//2]))
axis[3].set_xlabel('Frequency')
axis[3].set_ylabel('Amplitude')

plotter.show()
