# Display as many elements of the Fibonacci series as the user has specified. For example, if the input received the
# number 7, then the output should contain the first six numbers of the Fibonacci series: 1 1 2 3 5 8 13.


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


def fibonacci(x):
    if x < 3:
        return 1
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)


for i in range(num):
    i += 1
    print(str(fibonacci(i)))




# def fibonacci(x):
#     if x < 3:
#         return 1
#     else:
#         return fibonacci(x - 1) + fibonacci(x - 2)
#
#
# print(fibonacci(num))