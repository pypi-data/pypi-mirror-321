"""
Core implementation of Terry's mathematical system.
"""

import operator
import math
from functools import wraps

# Store original operations
_original_mul = operator.mul
_original_pow = math.pow

def terry_mul(a, b):
    """Terry multiplication: a × b = a + b copies of a"""
    return a + (_original_mul(b, a))

def terry_pow(x, y):
    """Terry power function using Terry multiplication"""
    if y == 0:
        return 1
    elif y == 1:
        return x
    elif y == 2:
        return terry_mul(x, x)
    else:
        result = x
        for _ in range(int(y) - 1):
            result = terry_mul(x, result)
        return result

def use_terryology(func):
    """Decorator that enables Terry mathematics within a function"""
    def wrapper(a, b):
        # Create namespace with Terry math
        terry_math = math.__dict__.copy()
        terry_math['pow'] = terry_pow
        namespace = {
            'math': type('TerryMath', (), terry_math),
            'a': a,
            'b': b
        }
        
        # For regular multiplication, use terry formula
        if func.__name__ == 'multiply':
            return eval(f"a + (b * a)", namespace)
        # For power, use terry_pow
        elif func.__name__ == 'power':
            return eval(f"math.pow(a, b)", namespace)
        
    return wrapper

@use_terryology
def multiply(a, b):
    """
    Perform multiplication according to Terry's system.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The result of a × b in Terry's system (a + b copies of a)
    """
    return a * b

@use_terryology
def power(a, b):
    """
    Compute powers according to Terry's system.
    
    Args:
        a: Base number
        b: Exponent
    
    Returns:
        The result of a^b in Terry's system
    """
    return math.pow(a, b)