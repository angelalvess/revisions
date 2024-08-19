def add_repr(cls):
    def __repr__(self):
        return f"<{cls.__name__} ({self.__dict__})>"
    cls.__repr__ = __repr__
    return cls


@add_repr
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("John", 30)
print(person)
