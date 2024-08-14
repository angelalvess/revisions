class Client:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old.')

    def adult(self):
        if self.age >= 18:
            print('I am an adult.')
        else:
            print(f'I am not an adult yet, I am {self.age} years old.')


angelina = Client('Angelina', 17)
angelina.introduce()
angelina.adult()
