# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 17:44:36 2024

@author: xiaoleiwww
"""
import matplotlib.pyplot as plt
import numpy as np
from generator.sequence import impulse_sequence, unit_step_sequence, rectangular_sequence, real_exponential_sequence
from generator.sequence import sinusoidal_sequence_math, sinusoidal_sequence_numpy


def main():
    # Define the range of k values
    k_values = np.arange(-10, 11)
    
    # Plot the sequences
    plt.figure(figsize=(15, 10))
    
    plt.subplot(3, 2, 1)
    plt.stem(k_values, [impulse_sequence(k) for k in k_values])
    plt.title('Impulse Sequence')
    
    plt.subplot(3, 2, 2)
    plt.stem(k_values, [unit_step_sequence(k) for k in k_values])
    plt.title('Unit Step Sequence')
    
    plt.subplot(3, 2, 3)
    plt.stem(k_values, [rectangular_sequence(k, 5) for k in k_values])
    plt.title('Rectangular Sequence (n=5)')
    
    plt.subplot(3, 2, 4)
    plt.stem(k_values, [real_exponential_sequence(k, 0.5) for k in k_values])
    plt.title('Real Exponential Sequence (a=0.5)')
    
    plt.subplot(3, 2, 5)
    plt.stem(k_values, [sinusoidal_sequence_math(k, 2*np.pi, 0.1).imag for k in k_values])
    plt.title('Imaginary Sequence (Math)')
    
    plt.subplot(3, 2, 6)
    plt.stem(k_values, [sinusoidal_sequence_numpy(k, 2*np.pi, 0.1).imag for k in k_values])
    plt.title('Imaginary Sequence (NumPy)')
    
    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__":
    main()