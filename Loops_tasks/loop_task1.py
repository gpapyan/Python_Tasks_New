# Count the even and odd digits of the entered natural number.
# For example, if the number 34560 is entered,
# then it has 3 even digits (4, 6, and 0) and 2 odd digits (3 and 5).


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
    even_count = 0
    odd_count = 0

    for i in range(len(stmt)):
        if int(stmt[i]) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print(f"Even numbers Count is {even_count}")
    print(f"Odd Numbers Count is {odd_count}")


result(num)
