# Fill an array of real numbers with keyboard input. Calculate the sum and product of the array of elements.
# Display the array itself, the resulting sum, and the product of its elements.


n = int(input("Enter number of elements : "))

inp_list = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]


total = 0
prod = 1
i = 0

while i < len(inp_list):
    total += inp_list[i]
    prod *= inp_list[i]
    i += 1


print(inp_list)
print(total)
print(prod)
