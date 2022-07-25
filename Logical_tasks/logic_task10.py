# Based on the lengths of three segments entered by the user,
# determine the possibility of the existence of a triangle composed of these segments.
# If such a triangle exists, then determine whether it is scalene, isosceles, or equilateral.

def validate(num):
    while True:
        try:
            int_num = int(input(num))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return int_num


a = validate("Please input a number : ")
b = validate("Please input b number: ")
c = validate("Please input c number: ")


def check(a, b, c):
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    else:
        return True


if check(a, b, c):
    def triangle(a, b, c):
        if a == b == c:
            print("Equilateral Triangle")
        elif a == b or b == c or c == a:
            print("Isosceles Triangle")
        else:
            print("Scalene Triangle")

    triangle(a, b, c)
else:
    print("Invalid")


