from util import add_category, add_transaction, total


food_category = add_category('Food')
rent_category = add_category('Rent')

food_transaction = add_transaction('Groceries', -100, food_category)
rent_transaction = add_transaction('Rent payment', 2000, rent_category)

total_value = total()
print(f'Total value: {total_value}')
