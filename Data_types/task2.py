# write a program that will take the length of the radius of the circle
# and will calculate the length of the area of
# the circle.

from math import pi


def validate(num):
    while True:
        try:
            num = float(input(num))
        except ValueError:
            print("Not a number! Try again.")
            continue
        else:
            return num


r = validate("Enter the radius of circle: ")
s = pi * r ** 2

print(s)
