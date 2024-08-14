
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    cpf: str
    age: int


@dataclass
class Student(Person):
    registration: str
    course: str


s1 = Student('João', '123.456.789-00', 20, '1234', 'Engenharia')
print(s1)
