# There is a list with arbitrary data. The task is to transform it into a set.
# If some elements cannot be hashed, then we skip them.
# The list_to_set () function prints out the given list and the resulting set.


inp_list = [25, 38, 'abc', [23, 758, 'aa'], 90, 'London', ['John', 34, 'Jimmy'], 78]

create_set = set()

for i in inp_list:
    try:
        create_set.add(i)
        continue
    except TypeError:
        pass

print(f"Your Given List is \n{inp_list}\n")
print(f"Your Set is \n{create_set}")
