# write a program that will solve the square equation.
import math


# ax*2 + bx + c

def validate(num):
    while True:
        try:
            int_num = int(input(num))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return int_num


a = validate("Enter the number of a: ")
b = validate("Enter the number of b: ")
c = validate("Enter the number of c: ")

# discriminant

d = b ** 2 - 4 * a * c

if d < 0:
    print("this equation has no real solution")
elif d == 0:
    x = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    print(f"has one solution {x}")
else:
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    print(f"has 2 solution {x1} and {x2}")
