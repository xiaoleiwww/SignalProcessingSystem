# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 19:59:05 2024

@author: xiaoleiwww

电容和电感的数值：

频率：AM广播的频率通常在中波范围内，约为 530 kHz 到 1700 kHz。因此，你需要选择适合于这一频率范围的电容和电感数值。
电容：电容的值应该足够大，以便在所需频率范围内提供所需的容抗。通常，电容的值在 pF 到 nF 的范围内。
电感：电感的值也应该足够大，以便在所需频率范围内提供所需的电感。通常，电感的值在 µH 到 mH 的范围内。

射频工程师工作笔记：https://www.zhihu.com/column/c_1668277589948018689
"""
import math
l = 0.1e-3
c = 0.5e-9
w = (1/l/c)**0.5
f = w/2/math.pi
print(f/1e3)