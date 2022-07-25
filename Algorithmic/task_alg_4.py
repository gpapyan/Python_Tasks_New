# Find all perfect numbers up to 10000. A perfect number is a number that is equal to the sum of all its
# divisors, except for itself. For example, the number 6 is perfect because itself is divisible by the numbers 1, 2,
# and 3, which add up to 6.


# def find_perfect(n: int):
#     sum_dgt = 1
#
#     i = 2
#     while i * i <= n:
#         if n % i == 0:
#             if i * i == n:
#                 sum_dgt += i
#             else:
#                 sum_dgt = sum_dgt + i + n / i
#         i += 1
#
#     return True if sum_dgt == n and n != 1 else False
#
#
# n = 2
# for n in range(10_000):
#     if find_perfect(n):
#         print(f" {n} is a perfect number")

def num_perfect(num: int):
    sum_dgt = 0
    for i in range(1, num):
        if num % i == 0:
            sum_dgt += i
    if num == sum_dgt:
        return sum_dgt
    else:
        return 0


for n in range(10_000):
    if num_perfect(n):
        print(f"{n} is a perfect number")
