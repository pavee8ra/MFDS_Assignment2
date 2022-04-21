import math
import numpy as np
import matplotlib.pyplot as plt

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

def get_frobeniusnorm(matrix,row,col):
    sumSq = 0

    for i in range(row):
        for j in range(col):
            sumSq += math.pow(matrix[i,j],2)

    print('Frobenius norm of the matrix through theoritical formula: ')
    print(math.sqrt(sumSq))

    print('Frobenius norm of the matrix through python linear algebra module: ')
    print(np.linalg.norm(matrix, 'fro'))

def f(A, b, x):
    error = np.dot(A, x) - b
    c = np.sum(error ** 2) / 2

    return c

def df(A, b, x):
    A_Trans = A.transpose()
    r = np.dot(A_Trans, np.dot(A, x)) - np.dot(A_Trans, b)
    
    return r

def gradient_descent(A, b, x, alpha, iter):

    next_x = x
    #print('i = 0 ; f(x)= '+str(f(A,b,next_x)))

    i = 0
    cvg = False
    res_x = []

    while i <= iter:
        
        x = next_x
        next_x = x - alpha * df(A, b, x)
        res_x[i] = np.linalg.norm(f(A, b, next_x), 2)

        #Convergence criteria
        if np.linalg.norm((next_x - x), 2) <= 0.001:
            cvg= True
            break

        i += 1
    
    if cvg:
        print('Minimum found in ' + str(i) + ' iterations')
        print('x = ', next_x)
    else:
        print('No convergence obtained for specified parameters')
            
    return res_x

print('Enter Mobile Number: ')
m: str = str(input())

if not m:
    m = mobileno

row, col = get_rowcol(m)
print('The dimensions of matrix is: ', row, 'x', col)

A = gen_matrix(row,col)
print('The random matrix generated is: ', A)
print(A.shape)

get_frobeniusnorm(A, row, col)

b = gen_vector(row)
print('The random vector generated is: ', b)
print(b.shape)

x = np.ones(col)
print('The x generated is: ', x)
print(x.shape)

alpha = 0.01
iter = 1000
res_x = gradient_descent(A, b, x, alpha, iter)

plt.plot(res_x, color='magenta', marker='o',mfc='pink' ) #plot the data
plt.xticks(range(0,len(res_x)+1, 1)) #set the tick frequency on x-axis

plt.ylabel('x-values') #set the label for y axis
plt.xlabel('index') #set the label for x-axis
plt.title("Plotting the gradient descent of given function") #set the title of the graph
plt.show() #display the graph