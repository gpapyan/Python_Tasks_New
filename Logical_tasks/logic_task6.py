# Enter two non-zero integers from the keyboard. Check if the first is divisible by the second. Display a message
# about it, display the remainder after the division (if any) and the integer part after the division (whatever).

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


def div(num1, num2):
    if num2 == 0:
        exit("Zero Division Error")
    else:
        qt = num1 // num2
        print(f"Quotient is {qt}")

        rm = num1 % num2
        print(f"Remainder is {rm}")


div(num1, num2)
