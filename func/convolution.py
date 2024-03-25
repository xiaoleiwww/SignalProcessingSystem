# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 15:31:21 2023

@author: xiaoleiwww
"""
import numpy as np

def conv_list(x, h):
    # Determine the length of the convolution result
    y_len = len(x) + len(h) - 1
    # Create the result array
    y = np.zeros(y_len)
    # Reverse h
    h = h[::-1]
    # Perform the convolution calculation
    for n in range(y_len):
        kmin = max(0, n - len(h) + 1)
        kmax = min(len(x), n + 1)
        for k in range(kmin, kmax):
            y[n] += x[k] * h[n - k]
        print('y[{}] = {}'.format(n, y[n]))
    return y


def conv_fft(x, h):
    # Calculate the length of the convolution result and ensure it's a power of 2
    n = len(x) + len(h) - 1
    n_fft = 1
    while n_fft < n:
        n_fft *= 2

    # Pad the input signals to length n_fft
    x_padded = np.pad(x, (0, n_fft - len(x)))
    h_padded = np.pad(h, (0, n_fft - len(h)))

    # Perform FFT on the signals
    X = np.fft.fft(x_padded)
    H = np.fft.fft(h_padded)

    # Compute the convolution result
    Y = X * H

    # Perform inverse FFT to get the convolution result in time domain
    y = np.fft.ifft(Y)

    # Retain the real part as the convolution result
    return np.real(y[:n])

def corr(x, y):
    x = [i for i in reversed(x)]
    return conv_fft(x, y)

def self_corr(x):
    return corr(x, x)


x = [-3, 4, 6, 0, -1]
h = [1, 1, 1, 1]
print(conv_list(x, h))
print(conv_fft(x, h))
x = [1, 2, 3, 4]
x1 = [4, 3, 2, 1]
y = [-1, 1, -2, 3]
print(self_corr(x))
print(conv_fft(x1, x))
print(corr(x, y))
print(corr(y, x))