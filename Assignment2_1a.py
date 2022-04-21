import math
import numpy as np

matrix = np.array([[3,-2,5],
                   [4,5,8],
                   [1,1,2],
                   [2,7,6]],float)

def main():

    print('-------------------------------------------------------------------------')
    print('Accepting entries for matrix: ')
    print('Enter number of rows: ')
    m: int = int(input())
    print('Enter number of columns: ')
    n: int = int(input())
    print('Enter number of significant digits to round off: ')
    d: int = int(input())

    if m<n:
        print('Number of rows must be greater than number of columns')

    matrix = np.random.normal(loc=0,scale=1,size=(m,n))
    sumSq = 0

    for i in range(m):
        for j in range(n):
            matrix[i,j] = round(matrix[i,j], d - int(math.floor(math.log10(abs(matrix[i,j])))) - 1)
            sumSq += math.pow(matrix[i,j],2)

    print("The random matrix generated is: ")
    print(matrix)

    print('The dimensions of the matrix is: ')
    print(matrix.shape)

    print('Frobenius norm of the matrix through theoritical formula: ')
    print(math.sqrt(sumSq))

    print('Frobenius norm of the matrix through python linear algebra module: ')
    print(np.linalg.norm(matrix, 'fro'))

main()