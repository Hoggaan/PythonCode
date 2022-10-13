from collections import namedtuple
from unicodedata import name

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

person = namedtuple('person', ['Magaca', 'Dada','Goobta'])
person1 = namedtuple('person1', 'Magaca Dada Goobta')
person2 = namedtuple('person2', "Magaca, dad, goobta")

prs = person('Axmed', 12, 'Cirka')
prs1 = person1('Calas',12, "Marka")
prs2 = person2("Samale", 12, "Salkudhaban")

print(prs1)
print(prs)
print(prs2)