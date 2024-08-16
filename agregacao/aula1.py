# total, inserir, listar

class Carrinho:

    def __init__(self):
        self.produtos = []

    def insert_products(self, *product):
        self.produtos.extend(product)

    def total(self):
        return sum([product.price for product in self.produtos])

    def list_products(self):
        for product in self.produtos:
            print(product.name, product.price)


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


p1 = Product('Camiseta', 50)
p2 = Product('Calça', 100)
car = Carrinho()
car.insert_products(p1)
car.insert_products(p2)
print(car.total())
car.list_products()
