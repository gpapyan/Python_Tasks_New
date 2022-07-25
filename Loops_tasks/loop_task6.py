# Form the inverse of the entered number in the order of the digits included in it and display it. For example,
# if you entered the number 3486, then you need to output the number 6843. Without using string methods.


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

rev = 0

while num > 0:
    a = num % 10
    rev = rev * 10 + a
    num = num // 10

print(f"Output is {rev}")
