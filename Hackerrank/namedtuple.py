from collections import namedtuple
from unicodedata import name

from sympy import true

# create a 2D tupe point as tuple 
point = (2,2)
#print(point)

#print(point[0], point[1]) # Access coordinates

# Try to update the coordinate values
#point[0] = 3
#point[2] = 4
# print(point)

# Named Tupple
# person = namedtuple('Person', "name children")
# Hassan = person("Hassan Elmi",["Abdifatah", "Aisho", "Dahira"])
# Hassan.children.append("Abdiaziz")
# print(Hassan.children)

# person = namedtuple('person', ['Magaca', 'Dada','Goobta'])
# person1 = namedtuple('person1', 'Magaca Dada Goobta')
# person2 = namedtuple('person2', "Magaca, dad, goobta")

# prs = person('Axmed', 12, 'Cirka')
# prs1 = person1('Calas',12, "Marka")
# prs2 = person2("Samale", 12, "Salkudhaban")

# print(prs1)
# print(prs)
# print(prs2)

# person = namedtuple('person', 'name age height')
# bahal = person._make(["Farah", [12, 13, 34], 34.5])
# print(bahal._asdict())

# # person = namedtuple('person', "Name Age Height Weight country", defaults=['Saudi'])
# # Xassan = person('Xassan', 12, 1.5, [50, 50, 50, 50])
# # for field, value in zip(Xassan._fields, Xassan):
# #     print(field, ' --> ',value)

# # print()
# # print(Xassan._field_defaults)

# import csv
# from collections import namedtuple

# with open('Hackerrank/data.csv','r') as csvfile:
#     reader = csv.reader(csvfile)
#     Employee = namedtuple('Employee', next(reader), rename = true)
#     for row in reader:
#         emp = Employee(*row)
#         print(emp.name, emp.job, emp.email)


#
from collections import namedtuple

num_studs = int(input())
stud_info = namedtuple('stud_info', input())

total_marks = 0
for i in range(num_studs):
    cur_info = stud_info(*input().split())
    total_marks += int(cur_info.MARKS)

print(total_marks/num_studs)
    
