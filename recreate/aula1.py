import json

PATH_FILE = 'data_recreate.json'


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('John', 24)
p2 = Person('Mary', 30)

db = [p1.__dict__, p2.__dict__]


with open(PATH_FILE, 'w') as file:
    json.dump(db, file, indent=4)
