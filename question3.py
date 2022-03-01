from sympy import *
from typing import Callable

def find_root(func : Callable[[float], float], a, b):
    x = Symbol('x')
    f_prime = diff(func)
    x_0 = b-a
    i=0
    while abs(func(x_0)) > 0.005:
        x_1 = x_0 - func(x_0)/f_prime(x_0)
        x_0 = x_1
    return x_0

def diff(f: Callable[[float], float]):
    x = Symbol('x')
    f_prime = f(x).diff(x)

    return(lambdify(x,f_prime))

if __name__ == '__main__':
    print(find_root(lambda x:x**2-4, 1,5))
    def f(x:int):
        return 2*x
    print(find_root(f, -1,1))