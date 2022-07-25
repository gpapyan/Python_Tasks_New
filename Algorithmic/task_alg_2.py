# Ten natural numbers greater than 2 are entered. Calculate how many primes are among them.

n = 10

num_prime = 0
not_prime = 0

inp_list = list(map(int, input("\nEnter 10 the numbers : ").strip().split()))[:n]

# check list, if 10num

while len(inp_list) <= n:
    if len(inp_list) >= n:
        break
    inp_list = list(map(int, input("\nEnter 10 the numbers : ").strip().split()))[:n]


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

print(f"Prime numbers Count is {num_prime}")

print(f"Not Prime numbers Count is {not_prime}")

print(inp_list)
