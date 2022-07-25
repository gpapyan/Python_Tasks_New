# Display the multiplication table (from 1 to 9)


def table(n, r):
    for i in range(1, r + 1):
        prod = 1
        prod = n * i
        print(f"{n} * {i} = {prod}")


num = 5

r = 9
table(num, r)
