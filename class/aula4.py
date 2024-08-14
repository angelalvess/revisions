from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    city: str

    def introduce(self):
        print(f'Hello, my name is {self.name} and I am {
              self.age} years old. I live in {self.city}.')


angelina = Person('Angelina', 17, 'São Paulo')
print(angelina)
angelina.introduce()
