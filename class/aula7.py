# getter e setter

from datetime import date


class Person:

    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    def get_age(self):
        return (date.today() - self.birth_date).days

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        if not isinstance(value, date):
            raise ValueError('birth_date must be a date object')
        self._birth_date = value


p1 = Person('João', date(1999, 1, 1))
print(p1.get_age())
print(p1.birth_date)
print()


class Person1():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError('age must be an integer')
        self._age = value


p2 = Person1('João',  '20')
print(p2.age)
