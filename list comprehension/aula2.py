price_list = [1700, 2100, 190, 200]

# sem list comprehension
new_price = []
for price in price_list:
    new_price.append(price * 2)
print(new_price)


# com list comprehension
duplicated_price_list = [price * 2 for price in price_list]
print(duplicated_price_list)


# com list comprehension e condicional
imposto = []
for price in price_list:
    if price >= 1000:
        imposto.append(price * 0.5)
print(imposto)

# com list comprehension e filter
imposto2 = [price * 0.5 for price in price_list if price >= 1000]
print(imposto2)
