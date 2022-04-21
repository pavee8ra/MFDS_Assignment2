import numpy as np
import math

def check_GramSchmidtAlg(a):
    calc_rank = np.linalg.matrix_rank(a)
    actual_rank = min(a.shape)

    if calc_rank >= actual_rank:
        print('Gram-Schmidt Algorithm can be applied on the input matrix')
        return True
    else:
        print('Gram-Schmidt Algorithm cannot be applied on given matrix')
        return False

def qr_factorization(A):
   
    m, n = A.shape
    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    add = 0
    mul = 0
    div = 0

    for j in range(n):
        v = A[:, j]
        for i in range(j - 1):
            q = Q[:, i]
            R[i, j] = q @ v
            mul += 1 #for matrix multiplication

            v = v - R[i, j] * q
            add += 1 #for addition/subtraction
            mul += 1 #for regular multiplication

        norm = np.linalg.norm(v)
        
        Q[:, j] = v / norm
        div += 1 #fo division of norm

        R[j, j] = norm

    print('Total Number of Additions performed: ', add)
    print('Total Number of Multiplications performed: ', mul)
    print('Total Number of Divisions performed: ', div)
    
    return Q, R

def find_frobenius_norm(A, Q, R):
    res = A - np.dot(Q, R)
    return np.linalg.norm(res, 'fro')

marix = np.random.normal(loc=0,scale=1,size=(7,5))

print('The matrix A is: ', marix)
bool_Result = check_GramSchmidtAlg(marix)

if bool_Result:
    Q, R = qr_factorization(marix)
    print ('The orthogonal matrix Q is: ', Q)

    print ('The upper triangular matrix R is: ', R)

    print('The frobenious norm of A-QR is: ', find_frobenius_norm(marix, Q, R))