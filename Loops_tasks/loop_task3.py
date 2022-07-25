# Print a series of natural numbers on the screen from minimum to maximum with a step.
# For example, if the minimum is 10, the maximum is 35, and the step is 5, then the output should be: 10 15 20 25 30 35.
# The user specifies the minimum, maximum, and step (read from the keyboard).


def validate(num):
    while True:
        try:
            int_num = int(input(num))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return int_num


min_num = validate("Enter the Minimum number: ")
max_num = validate("Enter the Maximum number: ")
step = validate("Enter the Step number: ")

print(f"The List of Natural Numbers from {min_num} to {max_num} and step is {step} are ")

for i in range(min_num, max_num + 1, step):
    print(i)
