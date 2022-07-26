# The user enters data on the number of students, their surnames, names, and scores each.
# The program should determine
# the average grade and display the last names and first names of students whose score is above the average.

students = {}


def averages(lst):
    return sum(lst) / len(lst)


while True:
    ids = input("enter your id: ")
    name = input("enter your name: ")
    surname = input("enter your surname: ")
    score = int(input("enter your score: "))

    students[ids] = [name, surname, score]

    repeat = input("would you like to add another student?" "(yes/no)")
    if repeat == 'no':
        break

print("\n**** List of Students ****")

print(students)

print("\n**** Result ****\n")

for ids, [name, surname, score] in students.items():
    print(f'ID -- {ids} -- {name} {surname} Your Score is: {score}')

score_lst = [score for ids, [name, surname, score] in students.items()]


avg = averages(score_lst)

highest = max(students, key=students.get)


print(f'AVG score is {avg}')
print(f'Highest Score Have {students[highest][0]} {students[highest][1]}')

