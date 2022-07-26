# Write a function to_dict () that takes a list argument and returns a dictionary in which each item in the list is
# both a key and a value. It is assumed that the elements of the list will follow the rules for specifying keys in
# dictionaries.

def to_dict(lst):
    keys = lst
    values = keys

    dictionary = dict(zip(keys, values))

    print(dictionary)


inp_list = list(input("\nEnter the numbers : ").strip().split())

to_dict(inp_list)
