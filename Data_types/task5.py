# Write a program that checks if a string is a palindrome or not.


pal = input("Enter the palindrome string: ")

w = ""
for i in pal:
    w = i + w

if (pal == w):
    print("The String is Palindrome")
else:
    print("The String is Not Palindrome")
