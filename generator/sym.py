# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 11:42:08 2024

@author: Lenovo
"""
from sympy import sequence, oo
from sympy.abc import n
import math
import numpy as np

def impulse_sequence():
    return sequence(1, (n, 0, 0))

def unit_step_sequence():
    return sequence(1, (n, 0, oo))
    
def ramp_sequence():
    return sequence(n, (n, 0, oo))
    
def rectangular_sequence(k):
    return sequence(1, (n, 0, k-1))

def real_exponential_sequence(a):
    return sequence(a**n, (n, 0, oo))

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
