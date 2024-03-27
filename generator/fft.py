# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 14:50:35 2024

@author: xiaoleiwww
"""

from sympy import fourier_transform, exp, cos
from sympy.abc import t, k
import numpy as np

def sp_fft(func):
    """
    Function using sympy for FFT. The frequncy function must be continuous, otherwise the critical point will not show.
    """
    # Using fourier_transform() method
    gfg = fourier_transform(func, t, k)
    return gfg

def fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = fft(x[::2])
    odd = fft(x[1::2])
    T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

# test
print(sp_fft(exp(-t**2)))
print(sp_fft(cos(t**2)))
x = np.array([1, 2, 3, 4])
result = fft(x)
print(result)
