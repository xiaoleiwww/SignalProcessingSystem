# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 14:50:35 2024

@author: Lenovo
"""

# import fourier_transform
from sympy import fourier_transform, exp, sin
from sympy.abc import x, k
 
# Using fourier_transform() method
gfg = fourier_transform(exp(-x**2), x, k)
gfg = fourier_transform(sin(x**2), x, k)
print(gfg)