# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 17:05:20 2024

@author: xiaoleiwww
"""
import math
import numpy as np

def impulse_sequence(k):
    if k == 0:
        return 1
    else:
        return 0

def unit_step_sequence(k):
    if k >= 0:
        return 1
    else:
        return 0
    
def ramp_sequence(k):
    if k >= 0:
        return k
    else:
        return 0
    
def rectangular_sequence(k, n):
    if k >= 0 and k <= n-1:
        return 1
    else:
        return 0

def real_exponential_sequence(k, a):
    return a**k

def imaginary_sequence_math(k, omega):
    real_part = math.cos(omega * k)
    imag_part = math.sin(omega * k)
    return complex(real_part, imag_part)

def imaginary_sequence_numpy(k, omega):
    return np.exp(1j * omega * k)

def sinusoidal_sequence_math(k, w, T):
    omega = w*T
    return imaginary_sequence_math(k, omega)

def sinusoidal_sequence_numpy(k, w, T):
    omega = w*T
    return imaginary_sequence_numpy(k, omega)