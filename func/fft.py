# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 14:50:35 2024

@author: xiaoleiwww
"""
import matplotlib.pyplot as plt
from sympy import fourier_transform, exp, cos
from sympy.abc import t, k
import numpy as np

def sp_ft(func):
    """
    Fourier transform using sympy. The frequncy function must be continuous, otherwise the critical point will not show.
    """
    # Using fourier_transform() method
    gfg = fourier_transform(func, t, k)
    return gfg

def fdfs(x):
    """
    Fast discrete Fourier series using Cooley-Tukey Algorithm. The input should be list.
    """
    N = len(x)
    if N <= 1:
        return x
    even = fdfs(x[::2])
    odd = fdfs(x[1::2])
    T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]


def dtft(x, omega):
    """
    Discrete-time Fourier transform. The input should be list.
    """
    N = len(x)
    n = np.arange(N)
    return np.sum(x * np.exp(-1j * omega * n))


# Test
print(sp_ft(exp(-t**2)))
print(sp_ft(cos(t**2)))
x = np.array([1, 2, 3, 4])
result = fdfs(x)
print(result)

x = np.array([1, 2, 1])
omega_values = np.linspace(-np.pi, np.pi*2, num=1000)
# Evaluate the DTFT for each frequency
X = np.array([dtft(x, omega) for omega in omega_values])

# Plot both magnitude and phase of DTFT
plt.figure(figsize=(12, 6))

# Plot magnitude
plt.subplot(1, 2, 1)
plt.plot(omega_values, np.abs(X), label='Magnitude')
plt.title('Magnitude of DTFT')
plt.xlabel('Frequency (radians)')
plt.ylabel('|X(e^{j\omega})|')
plt.grid(True)
plt.legend()

# Plot phase
plt.subplot(1, 2, 2)
plt.plot(omega_values, np.angle(X), label='Phase')
plt.title('Phase of DTFT')
plt.xlabel('Frequency (radians)')
plt.ylabel('Phase angle of X(e^{j\omega})')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()