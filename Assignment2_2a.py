import math
import numpy as np

mobileno = '7329107873'

def get_rowcol(mobile):
    
    for index, n in enumerate(mobile):
        if n == '0':
            n = '3'

    n1 = int(mobile[-4:-3])
    n2 = int(mobile[-3:-2])
    n3 = int(mobile[-2:-1])
    n4 = int(mobile[-1:])

    r = 10*n1+n2
    c = 10*n3+n4

    return r,c

def gen_matrix(r,c):
    matrix = np.random.normal(loc=0,scale=1,size=(r,c))

    return matrix

def gen_vector(r):
    vector = np.random.normal(loc=0,scale=1,size=(r,1))

    return vector

print('Enter Mobile Number: ')
m: str = str(input())

if not m:
    m = mobileno

row, col = get_rowcol(m)
print('The dimensions of matrix is: ', row, 'x', col)

A = gen_matrix(row,col)
print('The random matrix generated is: ', A)
print(A.shape)

b = gen_vector(row)
print('The random vector generated is: ', b)
print(b.shape)

sumSq = 0

for i in range(row):
    for j in range(col):
        sumSq += math.pow(A[i,j],2)

print('Frobenius norm of the matrix through theoritical formula: ')
print(math.sqrt(sumSq))

print('Frobenius norm of the matrix through python linear algebra module: ')
print(np.linalg.norm(A, 'fro'))