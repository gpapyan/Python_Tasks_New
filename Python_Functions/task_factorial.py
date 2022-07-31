def factorial(n):
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    return fact


num_fact = int(input("Enter Number of Fact: "))

print(f"Factorial of the number is:\n{factorial(num_fact)}")
