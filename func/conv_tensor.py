# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 15:34:55 2024

@author: xiaoleiwww
"""

import tensorflow as tf
import numpy as np

def convolution_fft(x, h):
    # Calculate the length of the convolution result
    n = len(x) + len(h) - 1

    # Pad the input signals
    x_padded = np.pad(x, (0, n - len(x)))
    h_padded = np.pad(h, (0, n - len(h)))

    # Convert signals to tensors
    x_tensor = tf.convert_to_tensor(x_padded, dtype=tf.float32)
    h_tensor = tf.convert_to_tensor(h_padded, dtype=tf.float32)

    # Reshape signals for convolution
    x_reshaped = tf.reshape(x_tensor, [1, -1, 1])
    h_reshaped = tf.reshape(h_tensor, [-1, 1, 1])

    # Perform convolution using TensorFlow
    y_tensor = tf.nn.conv1d(x_reshaped, h_reshaped, stride=1, padding='VALID')

    # Extract convolution result
    y = y_tensor.numpy().flatten()

    return y

# Test
x = np.array([-3, 4, 6, 0, -1])
h = np.array([1, 1, 1, 1])
print(convolution_fft(x, h))
