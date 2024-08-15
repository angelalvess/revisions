import json

PATH_FILE = 'recreate_data.json'


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Angel', 25)
p2 = Person('Eduardo', 30)
bd = [p1.__dict__, p2.__dict__]


with open(PATH_FILE, 'w') as file:
    json.dump(bd, file)
