import numpy as np

matrix = np.array([[3.0,-2.0,5.0],
                   [4.0,5.0,8.0],
                   [1.0,1.0,2.0],
                   [2.0,7.0,6.0]])

def check_GramSchmidtAlg(a):
    calc_rank = np.linalg.matrix_rank(a)
    actual_rank = min(a.shape)

    if calc_rank >= actual_rank:
        print('Gram-Schmidt Algorithm can be applied on the input matrix')
        return True
    else:
        print('Gram-Schmidt Algorithm cannot be applied on given matrix')
        return False

def gram_schmidt(A):
    
    (n, m) = A.shape
    Q = np.zeros((n, m))

    for i in range(m):
        
        q = A[:, i] # i-th column of A
        
        for j in range(i):
            q = q - np.dot(A[:, j], A[:, i]) * A[:, j]
        
        if np.array_equal(q, np.zeros(q.shape)):
            raise np.linalg.LinAlgError("The column vectors are not linearly independent")
        
        # normalize q
        q = q / np.sqrt(np.dot(q, q))
        
        # write the vector back in the matrix
        Q[:, i] = q
        
    return Q

print('The matrix A is: ', matrix)
bool_Result = check_GramSchmidtAlg(matrix)

if bool_Result:
    Q = gram_schmidt(matrix)
    print ('The orthogonal matrix Q is: ', Q)