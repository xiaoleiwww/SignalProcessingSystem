# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 14:50:35 2024

@author: xiaoleiwww
"""

from sympy import fourier_transform, exp, cos
from sympy.abc import t, k
import numpy as np

def sp_ft(func):
    """
    Fourier Transform using sympy. The frequncy function must be continuous, otherwise the critical point will not show.
    """
    # Using fourier_transform() method
    gfg = fourier_transform(func, t, k)
    return gfg

def fdfs(x):
    """
    Fast Discrete Fourier Series using Cooley-Tukey Algorithm. The input should be list.
    """
    N = len(x)
    if N <= 1:
        return x
    even = fdfs(x[::2])
    odd = fdfs(x[1::2])
    T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

# Test
print(sp_ft(exp(-t**2)))
print(sp_ft(cos(t**2)))
x = np.array([1, 2, 3, 4])
result = fdfs(x)
print(result)
