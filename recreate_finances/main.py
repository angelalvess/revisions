from util import create_category, create_transactions, total_value


hobby_category = create_category("Hobby")
food_category = create_category("Food")
recieve_category = create_category("Salary")

hobbie_transaction = create_transactions("Buy a book", -50, hobby_category)
food_transaction = create_transactions("Buy a pizza", -30, food_category)
recieve_transaction = create_transactions("Salary", 1000, recieve_category)


total = total_value()

print(total)
