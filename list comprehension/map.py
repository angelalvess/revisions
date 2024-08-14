# mapeamento


products = [
    {'name': 'p1', 'price': 13},
    {'name': 'p2', 'price': 55.55},
    {'name': 'p3', 'price': 5.59},
]


new_products = [{**product, 'price': product['price'] * 1.5}
                if product['price'] > 6 else {**product}

                for product in products]

print(*new_products, sep='\n')
