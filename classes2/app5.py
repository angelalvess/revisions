class Person:

    year = 2024

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birth_year(self):
        return Person.year - self.age


p1 = Person('John', 24)
print(p1.birth_year())
