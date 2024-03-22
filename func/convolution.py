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

x = [-3, 4, 6, 0, -1]
h = [1, 1, 1, 1]
print(conv_list(x, h))