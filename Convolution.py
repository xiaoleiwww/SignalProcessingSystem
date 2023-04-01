# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 15:31:21 2023

@author: xiaol
"""

import numpy as np

def convolution(x, h):
    # 确定卷积结果的长度
    y_len = len(x) + len(h) - 1
    # 创建结果数组
    y = np.zeros(y_len)
    # 反转h
    h = h[::-1]
    # 进行卷积计算
    for n in range(y_len):
        kmin = max(0, n - len(h) + 1)
        kmax = min(len(x), n + 1)
        for k in range(kmin, kmax):
            y[n] += x[k] * h[n - k]
        print('y[{}] = {}'.format(n, y[n]))
    return y

x = [-3, 4, 6, 0, -1]
h = [1, 1, 1, 1]
print(convolution(x, h))