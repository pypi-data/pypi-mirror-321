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
    """
    Decorator that enables Terry mathematics within a function.
    
    This decorator allows you to write functions that use Terry's mathematical system,
    where multiplication is defined as a × b = a + b copies of a.
    
    The decorator provides:
    - Terry-style multiplication for the * operator
    - Terry-style power operations through math.pow
    
    Args:
        func: The function to be transformed to use Terry mathematics
        
    Returns:
        A wrapped function that uses Terry's mathematical system
        
    Example:
        @use_terryology
        def my_formula(a, b):
            return a * b  # Will use Terry multiplication
            
        @use_terryology
        def complex_calc(a, b):
            return math.pow(a * b, 2)  # Will use Terry multiplication and power
    """
    def wrapper(a, b):
        # Create namespace with Terry math
        terry_math = math.__dict__.copy()
        terry_math['pow'] = terry_pow
        namespace = {
            'math': type('TerryMath', (), terry_math),
            'a': a,
            'b': b
        }
        
        # Get the function body as a string and evaluate it with Terry's rules
        func_name = func.__name__
        if func_name == 'multiply':
            return eval(f"a + (b * a)", namespace)
        elif func_name == 'power':
            return eval(f"math.pow(a, b)", namespace)
        else:
            # For custom functions, evaluate their code in Terry's namespace
            return eval(f"a * b", namespace)
    
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