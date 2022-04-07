"""creating matrices by different methods """

# 1st method by using for loops
def matrices_by_for_loop():
    rows = int(input("Enter the number of rows you want: "))
    columns = int(input("Enter the number of columns you want: "))
    matrix = []

    # sorting the inputs in correct manner of matrix
    for i in range(rows):
        a = []
        for j in range(columns):
            k = int(input())
            a.append(k)
        matrix.append(a)

    # printing the matrix
    for i in range(rows):
        for j in range(columns):
            print(matrix [i] [j], end = " ")
        print()


# 2nd method by using in-build function
from numpy import *
def in_build_method1():
    numbers = array([
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ])
    matrx = matrix(numbers)                 # to make array into matrix
    print(matrx)

def in_build_method2():
    matrx = matrix('1, 2, 3; 4, 5, 6')      # it is an 2*3 matrix in this rows get divided by ;
    print(matrx)

"""
 in matrix we can also use certain operations like for multiplication (M1 * M2) similarly for other mathematical fxn too
we can also use "max()" and "min()" in_build functions to get maximum and minimum values respectively 
to print diagonal matrix use "diagonal()" function
"""
