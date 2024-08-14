prices = [10, 20, 30]


def add_tax(price):
    return price * 1.1


# com for
prices_with_tax = []

for price in prices:
    prices_with_tax.append(add_tax(price))

print(prices_with_tax)


# com map
price_with_tax_map = list(map(add_tax, prices))
print(price_with_tax_map)
