import math
import numpy as np

import sympy as sy
from sympy import *
init_printing( use_latex='mathjax' )

import matplotlib.pyplot as plt

def construct_Polynomial(x,y):
    
    pe = 0
    pe = 7*x**3 - 3*x**2*y + 2*x*y**2 - 9*y**3 + 1*x**2 - 3*x*y + 7*y**2 - 8*x + 7*y - 3
    return pe

def find_CriticalPoints(pe, x, y):
    
    fx = sy.diff(pe, x)
    fy = sy.diff(pe, y)

    eq1 = sy.Eq(fx, 0)
    eq2 = sy.Eq(fy, 0)
    
    print(eq1)
    print(eq2)
    
    print(sy.solve(eq1))
    print(sy.solve(eq2))

    cp1 = sy.solve(eq1)[0][x].subs(y, 0)
    cp2 = sy.solve(eq1)[1][x].subs(y, 0)
    
    return fx, fy, cp1, cp2

x, y = sy.symbols('x y')

polynomial_eqn = construct_Polynomial(x,y)
fx, fy, cp1, cp2 = find_CriticalPoints(polynomial_eqn, x, y)

print('First derivative of x: ', fx)
print('First derivative of y: ', fy)

print('The critical points of the equation are: ', cp1, ', ', cp2)