"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math
def add(a, b): return a + b
<<<<<<< HEAD
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if a == 0: raise ZeroDivisionError
    return b / a
def log(a, b):
    if (a <= 0 or a == 1) or b <= 0: raise ValueError
    return math.log(b, a)
def exp(a, b): return a ** b
=======
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    else:
        return a / b
def logarithm(a, b):
    if (a <= 0) or (a == 1) or (b <= 0):
        raise ValueError
    return math.log(b, a)
def exponent(a, b): return a ** b
>>>>>>> c9c7d26c09f93e167e6d696cea630bae43ec561f
