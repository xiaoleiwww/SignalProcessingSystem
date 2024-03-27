# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:23:58 2024

@author: xiaoleiwww
"""

import numpy as np  
import matplotlib.pyplot as plt  
from scipy.signal import lfilter  
  
# set signal length  
N = 101  
  
# generate (-0.5, 0.5) uniformly distributed random numbers 
n = np.random.rand(N) - 0.5  
  
# generate time index
k = np.arange(N)  
  
# generate signal s
s = 2 * k * (0.9 ** k)  
  
# generate signal x
x = s + n  
  
# draw the original signal
plt.subplot(2, 1, 1)  
plt.plot(k, n, 'r-.', label='n[k]')  
plt.plot(k, s, 'b--', label='s[k]')  
plt.plot(k, x, 'g-', label='x[k]')  
plt.xlabel('Time index k')  
plt.legend()  
  
# set the length of the moving average filter
M = 5  
  
# calculate the coefficients of the moving average filter
b = np.ones(M) / M  
a = [1]  
  
# utilize filter
y = lfilter(b, a, x)  
  
# draw filtered signal
plt.subplot(2, 1, 2)  
plt.plot(k, s, 'b--', label='s[k]')  
plt.plot(k, y, 'r-', label='y[k]')  
plt.xlabel('Time index k')  
plt.legend()  
  
# show diagram
plt.tight_layout()  
plt.show()