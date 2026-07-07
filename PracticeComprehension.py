# marks = [45, 80, 65, 90, 33, 76]
# result=[mark for mark in marks if mark>=40]
# print(result)

# names = ["madhu", "milan", "bruce"]
# for idx, name in enumerate(names):
#     names[idx] = name.upper()
# print(names)

# use map instead of a for-based comprehension
# result_2 = list(map(str.upper, names))
# result=[name.upper() for name in names]
# print(result)
# employees = {
#     "Madhu": 50000,
#     "Milan": 60000,
#     "Bruce": 75000
# }

# set of salary increases (10% of each salary)
# salary_increase = {name: salary * 1.10 for name, salary in employees.items()}
# print(salary_increase)
# numbers = [1,2,3,4,5]

# my_set={n*n for n in numbers}
# print(my_set)
students = [
    {"name":"A","marks":80},
    {"name":"B","marks":30},
    {"name":"C","marks":90}
]
for item in students:
    name = item["name"]
    marks = item["marks"]
    if marks > 50:
        print(name)


# print(students)
# result_dict = list(filter(lambda student: student["marks"] >= 50, students))
result_dict=[student for student in students if student["marks"]>=50]
print(result_dict)


