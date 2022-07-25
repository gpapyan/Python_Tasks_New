# Write a program that will take 2 numbers and will return True
# if the first number is greater than or equal to the
# other and will return False otherwise

def validate(num):
    while True:
        try:
            num = float(input(num))
        except ValueError:
            print("Not a number! Try again.")
            continue
        else:
            return num


num1 = validate("Enter the first number: ")
num2 = validate("Enter the second number: ")

tf = True if num1 >= num2 else False

print(tf)
