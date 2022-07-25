# Write a program that will take a five-digit number and
# will insert each digit in the given number
# in one list in order from beginning to end.

def validate(num):
    while True:
        try:
            int_num = int(input(num))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return int_num


digit = validate("Input five-digit number: ")

lst = []

while len(str(digit)) != 5:
    digit = validate("Input five-digit number: ")
    if len(str(digit)) == 5:
        break

if len(str(digit)) == 5:
    for i in str(digit):
        lst.append(i)
    print(lst)
else:
    print("Incorrect input")

