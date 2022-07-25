# Write a function that will get a non-negative number matrix.
# Calculate the sum of the elements in each column.
# Determine which column contains the maximum amount.

import random

low = 1
high = 100
cols = 3
rows = 3

matrx = [random.choices(range(low, high), k=cols) for _ in range(rows)]

print(matrx)


# Function to calculate sum of each row
def row_sum(mtx):
    sum_of = 0
    stmt = []

    print("\nSum of each row:\n")

    for i in range(cols):
        for j in range(rows):
            sum_of += mtx[i][j]

        print(f"Sum of The Row {i} = {sum_of}")
        stmt.append(sum_of)

        sum_of = 0

    print(f"\nMax Sum of The Row = {max(stmt)}")


def column_sum(mtx):
    sum_of = 0
    stmt = []

    print("\nSum of each column:\n")

    for i in range(cols):
        for j in range(rows):
            sum_of += mtx[j][i]
        print(f"Sum of The Column {i} = {sum_of}")
        stmt.append(sum_of)
        sum_of = 0

    print(f"\nMax Sum of The Column = {max(stmt)}")


row_sum(matrx)
column_sum(matrx)


