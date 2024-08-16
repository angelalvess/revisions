class Car:
    def __init__(self, name):
        self.name = name
        self.motor = None
        self.fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, value):
        self._motor = value

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, value):
        self._fabricante = value


class Motor:
    def __init__(self, name):
        self.name = name

    def motor_name(self):
        return f'The car have the motor {self.name}'


class Fabricante:
    def __init__(self, name):
        self.name = name

    def fabricate_by(self):
        return f'The car is fabricated by {self.name}'


c1 = Car('Fusca')
m1 = Motor('78as778')
f1 = Fabricante('Volkswagen')

c1.motor = m1
c1.fabricante = f1
print(c1.motor.motor_name())
print(c1.fabricante.fabricate_by())

print(c1.name)
print(c1.motor.name)
print(c1.fabricante.name)
