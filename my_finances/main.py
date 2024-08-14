from util import create_category, create_transactions, total_value

recieve_category = create_category("Recieve")
food_category = create_category("Food")
hobby_category = create_category("Hobby")

transaction1 = create_transactions("Salary", 5000, recieve_category)
transaction2 = create_transactions("Buy food", -100, food_category)
transaction3 = create_transactions("Buy book", -50, hobby_category)

total = total_value()

print(total)
