# Write a program (calculator) that will accept 2 numbers and an action(+, -, *, /, **) , the program must return the
# result of the given action. for example num_1 = 3 num_2 = 5 action = ' + ' result = 8

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
act = input("Enter action(+, -, *, /, **) : ")

if act == "+":
    sum = num1 + num2
    print(f"Your answer is {num1} {act} {num2} = {sum}")
elif act == "-":
    sum = num1 - num2
    print(f"Your answer is {num1} {act} {num2} = {sum}")
elif act == "*":
    sum = num1 * num2
    print(f"Your answer is {num1} {act} {num2} = {sum}")
elif act == "/":
    sum = num1 / num2
    print(f"Your answer is {num1} {act} {num2} = {sum}")
elif act == "**":
    sum = num1 ** num2
    print(f"Your answer is {num1} {act} {num2} = {sum}")
else:
    print("Incorrect action")
