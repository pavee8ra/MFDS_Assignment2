import math
import numpy as np

mobileno = '7329107873'
polynomial_degree = ['x^3', 'x^2y', 'xy^2', 'y^3', 'x^2', 'xy', 'y^2', 'x', 'y', '']

def construct_Polynomial(m, pd):
    
    pe = ''

    for index, v in enumerate(m):
        if v == '0':
            v = '3'
        t = v + pd[index]
        
        if index == 0:
            pe += t
        elif index % 2 == 0:
            pe += '+'+t
        else:
            pe += '-'+t

    return pe

polynomial_eqn = construct_Polynomial(mobileno, polynomial_degree)

print(polynomial_eqn)