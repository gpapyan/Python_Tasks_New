# In the entered interval of natural numbers,
# find those whose number of divisors is not less than the entered value.
# For the found numbers, display the number of divisors and all divisors.


def validate(num):
    while True:
        try:
            int_num = int(input(num))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return int_num


len_list = validate("Enter len of list: ")

inp_list = list(map(int, input(f"\nEnter {len_list} the numbers : ").strip().split()))[:len_list]

# check input len

while len(inp_list) <= len_list:
    if len(inp_list) >= len_list:
        break
    inp_list = list(map(int, input(f"\nEnter {len_list} the numbers : ").strip().split()))[:len_list]

print(f"{inp_list} \n")


def divisors(n):
    result = set()
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            result.add(i)
            result.add(n//i)
        else:
            result.add(1)
    return list(result)


for nm in inp_list:
    print(divisors(nm))
    if len_list <= len(divisors(nm)):
        print(f"Entered lenght of list lt or Equal to Num of Divisors -- {nm} ")
    else:
        print(f"Entered lenght of list gt then Num of Divisors -- {nm} ")


# print(divisors(36))
