from aula1 import Person, PATH_FILE

import json

with open(PATH_FILE, 'r', encoding='utf-8') as file:
    data = json.load(file)
    p1 = Person(**data[0])

    print(p1.name)
