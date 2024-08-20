import account


class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}({self.name}, {self.age})'


class Client(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.account: account.Account | None = None


if __name__ == '__main__':
    print('Client')
    client = Client('John', 30)
    client.account = account.CreditAccount(1111, 2222, 1000, 1000)
    print(client)
    print(client.account)
