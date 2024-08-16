# inserir endereco, listar enderecos


class Client:

    def __init__(self, name):
        self.name = name
        self.addresses = []

    def insert_address(self, street, number):
        self.addresses.append(Adress(street, number))

    def list_adresses(self):
        for address in self.addresses:
            print(address.street, address.number)


class Adress:

    def __init__(self, street, number):
        self.street = street
        self.number = number


client1 = Client('João')
client1.insert_address('Rua A', '123')
client1.insert_address('Rua B', '321')

client1.list_adresses()
