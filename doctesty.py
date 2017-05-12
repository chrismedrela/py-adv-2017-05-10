import doctest
import math

def factorial(n):
    '''
    Doc djafhdajf
    >>> factorial(1)
    1
    >>> factorial(3)
    6
    >>> factorial(4)
    12
    '''

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)