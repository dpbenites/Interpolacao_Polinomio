import numpy as np
from scipy.linalg import inv

coord_list = [ (0,1) , (1,6) , (2,5) , (3,24) , (4,6), (5,10)]


def Operation(coord_list:list):
    n      = len(coord_list) # order of the polynomial function
    x_list = []
    y_list = []

    ## access of x values and y values 

    for i in range(n):
        ##
        x_list.append(coord_list[i][0])
        y_list.append(coord_list[i][1])
    
    y_array = np.array(y_list)
    y_array = y_array.reshape(-1,1)

    x_array = np.zeros( (n, n) ) # creating a null array to put the x`s coordinates

    for row in range(n):
    ## x1 --> iteracao 1
        for column in range(n):
            ## x_list[row] -> x1
            ## x1** column --> 1 , x_1^1, x_1² , x_1³ ,... x_1^n
            
            x_array[row , column] = x_list[row] ** column
    
    x_inv = inv(x_array)
    coef_matrix = x_inv @ y_array

    ## return a tuple wich the 0 index corresponds to the coef_matrix
    return (coef_matrix, np.array(x_list), np.array(y_list))


def func(array , x):
    n = array.shape[0]
    p_x = 0

    for i in range(n):

        p_x += array[i][0]*x**i
    
    return p_x


def polinomial(array, x):
    '''
    parameters: 
    array: column matrix or ndrray(n,1) dimension

    return:
      a polinomial function and its points as array

    '''

    n = array.shape[0] # grau do polinomio
    y = []

    for i in range(len(x)):
        y.append(func(array, x[i]))
    
    return np.array(y)
