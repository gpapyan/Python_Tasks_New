# Enter a date from the keyboard (for example, 1986).
# Decide whether the year entered by the user is a leap year or not.

def validate(num):
    while True:
        try:
            int_num = int(input(num))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return int_num


year = validate("Enter a date of year: ")

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")