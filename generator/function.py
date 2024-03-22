# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 17:05:20 2024

@author: xiaoleiwww
"""
import sympy as sp

class func:
    def __init__(self, symbol):
        if isinstance(symbol, str):
            self.x = sp.symbols(symbol)
        else:
            self.x = sp.symbols("x")
        self.y = 0
    
    def symbol(self):
        return self.x
    
    def change(self, symbols):
        # Change function expression
        self.y = symbols
        return self.y
    
    def diff(self):
        # Differentiate
        return sp.diff(self.y, self.x)
    
    def integrate(self):
        # Integrate
        return sp.integrate(self.y, self.x)
    
    def fourier_transform(self):
        omega = sp.symbols("omega")
        F = sp.fourier_transform(self.y, self.x, omega)
        return F

class signals:
    def __init__(self):
        self.ft = func("t")
    
    def sin(self):
        return self.ft.change(sp.sin(self.ft.symbol()))
    
    def sinw(self, w):
        return self.ft.change(sp.sin(w*self.ft.symbol()))
    
    def cos(self):
        return self.ft.change(sp.cos(self.ft.symbol()))
    
    def cosw(self, w):
        return self.ft.change(sp.cos(w*self.ft.symbol()))
    
    def tan(self):
        return self.ft.change(sp.tan(self.ft.symbol()))
    
    def tanw(self, w):
        return self.ft.change(sp.tan(w*self.ft.symbol()))
    

if __name__ == "__main__":
    
    ft = func("t")
    x = ft.symbol()
    y = x*x*x + x
    
    print(y)
    print(ft.change(y))
    
    print(type(x))
    print(type(y))
    
    print(ft.diff())
    print(ft.diff().diff())
    
    print(ft.integrate())
    
    print(signals().sin())
    print(signals().sinw(10))
    print(signals().cos())
    print(signals().cosw(10))
    print(signals().tan())
    print(signals().tanw(10))
    
    y = signals().tanw(10)
    ft.change(y)
    
    print(ft.fourier_transform())