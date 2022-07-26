# The to_set () function receives a string or a list of numbers as input. Convert them to many.
# The output should be a set, its length, and length is the initial length of the string or list.

def convert(string):
    # lengths = len(string.split(" "))
    li = set(string.split(" "))
    return li, f"length of set is {len(li)}"


str1 = "length string and length of set"

print(f"Length input string {len(str1)}")
print(convert(str1))
