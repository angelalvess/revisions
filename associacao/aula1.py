# associar 2 classes


class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self.ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class Ferramenta:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo...'


escritor = Escritor('João')
caneta = Ferramenta('Canetaa')
escritor.ferramenta = caneta

print(escritor.ferramenta)
print(escritor.ferramenta.escrever())


class Person:

    def __init__(self, name):
        self.name = name
        self.food = None

    @property
    def food(self):
        return self._food

    @food.setter
    def food(self, food):
        self._food = food


class Food:

    def __init__(self, name):
        self.name = name

    def eat(self):
        return f'{self.name} is good as fuck...'


p1 = Person('João')
food1 = Food('Pizza')
p1.food = food1

print(p1.food.eat())
