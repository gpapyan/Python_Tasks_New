# In the entered interval of natural numbers,
# find those whose number of divisors is not less than the entered value.
# For the found numbers, display the number of divisors and all divisors.

inp_list = []
len_list = int(input("Enter The List Size: "))

for i in range(0, len_list):
    print(f"Enter Number -- {i + 1}")
    item = int(input())
    inp_list.append(item)


def divisors(n):
    result = set()
    for a in range(2, int(n**0.5)+1):
        if n % a == 0:
            result.add(a)
            result.add(n//a)
        else:
            result.add(1)
    return list(result)


value_div = int(input('Enter Value of divisors: '))

for nm in inp_list:
    if value_div <= len(divisors(nm)):
        print(f"\nNumber of divisors is not less than the entered value -- {nm}")
        print(divisors(nm))
    else:
        print("\nNumber of divisors is less than the entered value")
        break


