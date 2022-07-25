# 1.	Write a function that will generate a matrix whose elements are '*', change the elements of the diagonal of
# the matrix, '#' symbol.

matrix = []

range_of = int(input("Input range of Matrix: "))

for i in range(range_of):
    row = ['*' for _ in range(range_of)]
    matrix.append(row)
    matrix[i][i] = "#"

print(matrix)
