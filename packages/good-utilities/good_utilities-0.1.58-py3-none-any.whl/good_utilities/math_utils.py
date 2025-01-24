# Math utility functions


import math


def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.
    
    Parameters:
        n (int): A non-negative integer for which the factorial is to be computed.
    
    Returns:
        int: The factorial of the given integer n, or raises a ValueError if n is negative.

    Imports:
        import math
    """
    if n < 0:
        raise ValueError('n must be a non-negative integer')
    return math.factorial(n)


def gcd(a: int, b: int) -> int:
    """
    Calculate the greatest common divisor (GCD) of two integers.
    
    Parameters:
        a (int): The first integer.
        b (int): The second integer.
    
    Returns:
        int: The greatest common divisor of a and b.

    Imports:
        import math
    """
    while b:
        a, b = b, a % b
    return abs(a)
