""" performing the additions and subtraction of the matrices manually """

# creating matrices
def matrix(m,n):
    final_matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            inp = int(input(f"(Enter the input for matrices final_matrix[{i}][{j}]")) # to take inputs of matrices position wise
            row.append(inp)
        final_matrix.append(row)
    return final_matrix

# function to do addition of the matrices
def sum(A, B):
    final_sum = []
    for i in range(len(A)):                 # it will count the number of Rows in matrix
        row = []
        for j in range(len(A[0])):          # it will count the number of Columns in matrix
            row.append(A[i][j] + B[i][j])
        final_sum.append(row)
    return final_sum

# function to do subtraction of the matrices
def subtraction(A, B):
    final_subtraction = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] - B[i][j])
        final_subtraction.append(row)
    return final_subtraction

m = int(input("Enter the number of Rows: "))
n = int(input("Enter the number of Columns: "))

print("Enter matrix A values")
A = matrix(m, n)
print(A)

print("Enter matrix B values")
B = matrix(m, n)
print(B)

summing = sum(A, B)
print("Sum of matrix A and B is: ",summing)

sub = subtraction(A, B)
print("Subtraction of matrix A and B is: ", sub)
