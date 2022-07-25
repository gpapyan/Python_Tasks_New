# Find the sum and product of the digits of the entered natural number. For example, if the number 325 is entered,
# then the sum of its digits is 10 (3+2+5), and the product is 30 (325).


def validate(num):
    while True:
        try:
            int_num = int(input(num))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return int_num


num = validate("Please input number : ")


# Product of digits

def product(num):
    product = 1

    while num != 0:
        product = product * (num % 10)
        num //= 10
    return product


print(product(num), " is Product of digits \n")


# Summ of digits

def sum(num):
    sum = 0

    while (num != 0):
        sum = sum + int(num % 10)
        num = int(num / 10)
    return sum


print(sum(num), " is Sum of digits")
