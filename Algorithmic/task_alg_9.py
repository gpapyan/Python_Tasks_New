# Write a function that gets a number, not a negative integer, and subtract all its odd digits.
# If all digits are subtracted,
# return zero. Example:
#
# number = 123456, the output should be 246
# number = 139, the output must be 0


def validate(num):
    while True:
        try:
            int_num = int(input(num))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return int_num


num = validate("Enter the number: ")


def result(n):
    stmt = str(n)
    even_num = []
    odd_count = 0

    for i in range(len(stmt)):
        if int(stmt[i]) % 2 == 0:
            even_num.append(stmt[i])
        else:
            odd_count += 1
    if len(even_num) == 0:
        print(f"Even Numbers List is Empty")
    else:
        print(f"Even numbers list is {even_num}")

    print(f"Odd Numbers Count is {odd_count}")


result(num)
