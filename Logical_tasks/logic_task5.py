# Enter two random numbers from the keyboard, one even and the other odd.
# Decide and display an odd number.


def validate(num):
    while True:
        try:
            int_num = int(input(num))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return int_num


num1 = validate("Enter the first number: ")
num2 = validate("Enter the second number: ")

if num1 % 2 != 0:
    print(f"{num1} is Odd")
elif num2 % 2 != 0:
    print(f"{num2} is Odd")
else:
    print(f"{num1} and {num2} is Even")
