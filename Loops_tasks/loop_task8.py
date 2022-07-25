# Fill one array with random numbers, the other with numbers entered from the keyboard, and write the sums of the
# corresponding cells of the first two in the cells of the third. Display the contents of the arrays on the screen.

import random

# lst = []
#
# n = int(input("Enter number of elements : "))
#
#
# for i in range(0, n):
#     ele = int(input())
#
#     lst.append(ele)
#
# print(lst)

n = int(input("Enter number of elements : "))

inp_list = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]


new_lst = [i for i in range(1, 100)]
rand_list = random.choices(new_lst, k=n)

# Sum of 2 list

sum = [x + y for x, y in zip(inp_list, rand_list)]

print(inp_list)
print(rand_list)
print(sum)

