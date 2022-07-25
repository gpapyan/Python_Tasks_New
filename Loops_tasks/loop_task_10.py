# Write a program that will add, subtract, multiply, or divide two numbers. The numbers and signs of the operation are
# entered by the user. After completing the calculation, the program should not terminate but should request new data for calculations.
# The end of the program must be carried out by entering the character '0' as an operation character.
# If the user enters an invalid character (not ‘0’, ‘+’, ‘-’, ‘*’, ‘/’),
# then the program should inform him about the error and ask again for the character of the operation.
# Also, inform the user about the impossibility of dividing by zero if he entered 0 as a divisor.

def validate(num):
    while True:
        try:
            inp_num = float(input(num))
        except ValueError:
            print("Not a number! Try again.")
            continue
        else:
            return inp_num


num1 = validate("Enter the first number: ")
num2 = validate("Enter the second number: ")
act = input("Enter action(+, -, *, /), or zero to exit : ")

while act != "+" or act != "-" or act != "*" or act != "/" or act != "0":
    act = input("Enter action(+, -, *, /), or zero to exit : ")
    if act == "+" or act == "-" or act == "*" or act == "/" or act == "0":
        break

if act == "0":
    exit("You enter the Exit Code, Bye")
elif act == "+":
    sum = num1 + num2
    print(f"Your answer is {num1} {act} {num2} = {sum}")
elif act == "-":
    sum = num1 - num2
    print(f"Your answer is {num1} {act} {num2} = {sum}")
elif act == "*":
    sum = num1 * num2
    print(f"Your answer is {num1} {act} {num2} = {sum}")
elif act == "/":
    if num2 == 0:
        exit("Zero Division Error, Bye")
    else:
        sum = num1 / num2
        print(f"Your answer is {num1} {act} {num2} = {sum}")
else:
    print("Incorrect action")