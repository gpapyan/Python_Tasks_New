# Generate 20 random integers ranging from -5 to 4, and write them to the array cells.
# Count how many of them are positive, negative, and zero values. Display array elements and counted quantities.


import random


def rand(start, end, num):
    res = []

    for j in range(num):
        res.append(random.randint(start, end))

    return res


num = 20
start = -5
end = 4

lis_num = rand(start, end, num)


neg_count = 0
pos_count = 0
zero_count = 0

for i in range(20):
    if lis_num[i] < 0:
        neg_count += 1
    elif lis_num[i] > 0:
        pos_count += 1
    else:
        zero_count += 1



print(lis_num)
print(f"Negativ numbers Count is {neg_count}")
print(f"Positive Numbers Count is {pos_count}")
print(f"Zero Numbers Count is {zero_count}")
