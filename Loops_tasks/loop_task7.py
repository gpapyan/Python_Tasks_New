# The program generates a random integer from 0 to 100. The user must guess it in no more than 10 attempts.
# After each unsuccessful attempt, more or less the number entered by the user should be reported than what is guessed.
# If in 10 attempts the number is not guessed, then output the hidden number.

from random import randint


def validate(num):
    while True:
        try:
            int_num = int(input(num))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return int_num


num = randint(0, 100)

i = 0

while i < 10:
    digit = validate("Enter the Number: ")
    if digit == num:
        print("Your entered number equal to random number")
        break
    elif digit < num:
        print("Your entered number lT random number")
    elif digit > num:
        print("Your entered number gT random number")
    i += 1

print("All Done")
