import random

low = 1
high = 100
cols = 3
rows = 3

matrx = [random.choices(range(low, high), k=cols) for _ in range(rows)]

print(f"{matrx} \n")


def row_sum(mtx, i):
    print(f"\nSum of {i} row:")

    if i in range(len(mtx)):
        sum_of = sum(mtx[i])
        print(sum_of)
    else:
        print('You entered wrong index')


def max_sum(mtx):
    maximum_sum = 0
    sum_of = 0
    for i in range(len(mtx)):
        for j in range(len(mtx[i])):
            sum_of += mtx[i][j]

            if sum_of > maximum_sum:
                maximum_sum = sum_of
        sum_of = 0
    return f"\nMaximum Sum of Rows is {maximum_sum}"


inp_index = int(input("Enter Row index: "))

row_sum(matrx, inp_index)
print(max_sum(matrx))
