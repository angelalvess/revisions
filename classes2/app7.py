class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_without_name(cls, age):
        return cls('Without Name', age)

    @classmethod
    def create_with_15(cls, name):
        return cls(name, 15)


p1 = Person.create_without_name(25)
p2 = Person.create_with_15('John')
print(p1.name, p1.age)
