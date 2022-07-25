# Enter three integers from the keyboard. Decide which is the biggest.

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
num3 = validate("Enter the third number: ")

if num1 < num2 > num3:
    print(num2)
elif num1 > num3:
    print(num1)
elif num2 < num3:
    print(num3)
else:
    print("The numbers are equal each other")
