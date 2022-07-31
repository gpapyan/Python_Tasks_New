# Ten natural numbers greater than 2 are entered. Calculate how many primes are among them.

inp_list = []
n = int(input("Enter The List Size: "))

for i in range(0, n):
    print(f"Enter Number -- {i + 1}")
    item = int(input())
    inp_list.append(item)


num_prime = 0
not_prime = 0

for num in inp_list:

    if num > 1:
        for i in range(2, int(num / 2) + 1):

            if (num % i) == 0:
                not_prime += 1
                break
        else:
            num_prime += 1
    else:
        not_prime += 1

print(f"\nPrime numbers Count is {num_prime}")

print(f"\nNot Prime numbers Count is {not_prime} \n")

print(inp_list)
