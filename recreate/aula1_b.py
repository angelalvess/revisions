import json
from aula1 import PATH_FILE, Person


with open(PATH_FILE, 'r') as file:
    data = json.load(file)
    p1 = Person(**data[0])
    p2 = Person(**data[1])

    print(p1.name, p1.age)
    print(p2.name, p2.age)
