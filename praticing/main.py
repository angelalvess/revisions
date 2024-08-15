from utils import create_category, create_transactions, total_value


food_category = create_category('Food')
hobby_category = create_category('Hobby')
salary_category = create_category('Salary')
t1 = create_transactions('Bought a pizza', -50, food_category)
t2 = create_transactions('Bought a soda', -5, food_category)
t3 = create_transactions('Bought a burger', -15, food_category)
t4 = create_transactions('Bought a book', -20, hobby_category)
t5 = create_transactions('Bought a game', 3000, salary_category)


total = total_value()
print(f'Total value: {total}')
