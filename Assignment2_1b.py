import math
import numpy as np

matrix = np.array([[3,-2,5],
                   [4,5,8],
                   [1,1,2],
                   [2,7,6]],float)

def check_GramSchmidtAlg(a):
    calc_rank = np.linalg.matrix_rank(a)
    actual_rank = min(a.shape)

    if calc_rank >= actual_rank:
        print('Gram-Schmidt Algorithm can be applied on the input matrix')
        return True
    else:
        print('Gram-Schmidt Algorithm cannot be applied on given matrix')
        return False

bool_Result = check_GramSchmidtAlg(matrix)