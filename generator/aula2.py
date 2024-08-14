import copy


products = [
    {'name': 'Produto 1', 'price': 100},
    {'name': 'Produto 2', 'price': 500},
    {'name': 'Produto 3', 'price': 300},
    {'name': 'Produto 4', 'price': 90},
    {'name': 'Produto 5', 'price': 60},
]

print(*products, sep='\n')
print('---')


new_products = [
    {**product, 'price': product['price'] * 1.5}
    for product in copy.deepcopy(products)
]

print(*new_products, sep='\n')

print('---')


order_price = sorted(copy.deepcopy(products),
                     key=lambda item: item['price'], reverse=True)

order_name = sorted(copy.deepcopy(products),
                    key=lambda item: item['name'])


def show(lista):
    for item in lista:
        print(item)


show(order_price)
print()
show(order_name)
