# Display a "rectangle" made up of two types of symbols.
# The outline of the rectangle should consist of one symbol,
# and in the "fill" - from another.


def rectangle(n, m, symbols):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 or i == n or j == 1 or j == m:
                print(symbols, end="")
            elif i == 1 or i == n or j == 1 or j == m:
                print("*", end="")
            else:
                print(" ", end="")

        print()


rows = int(input("Enter Row of Rectangle: "))
columns = int(input("Enter Column of Rectangle: "))
symbol = input("Enter Symbol of Rectangle: ")

rectangle(rows, columns, symbol)
