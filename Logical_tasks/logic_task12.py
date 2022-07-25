# Determine the quarter of the coordinate plane to which the point belongs.
# Enter point coordinates from the keyboard


def validate(num):
    while True:
        try:
            int_num = int(input(num))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return int_num


x = validate("Enter the X number: ")
y = validate("Enter the Y number: ")


def quadrant(x, y):
    if x > 0 and y > 0:
        print("lies in First quadrant")
    elif x < 0 and y > 0:
        print("lies in Second quadrant")
    elif x < 0 and y < 0:
        print("lies in Third quadrant")
    elif x > 0 and y < 0:
        print("lies in Fourth quadrant")
    else:
        print("lies at origin")

quadrant(x, y)