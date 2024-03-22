# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 11:42:08 2024

@author: xiaoleiwww
"""
from sympy import sequence, oo, Piecewise, cos, sin
from sympy.abc import n

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

def imaginary_sequence(k, omega):
    real_part = Piecewise((cos(omega * k), True))
    imag_part = Piecewise((sin(omega * k), True))
    return sequence(real_part + imag_part * 1j, (n, 0, oo))

def sinusoidal_sequence(k, w, T):
    omega = w*T
    return imaginary_sequence(k, omega)