from category import Category
from transactions import Transactions


CREATE_CATEGORY = []
CREATE_TRANSACTIONS = []


def create_category(category):
    new_category = Category(category)
    CREATE_CATEGORY.append(new_category)
    return new_category


def create_transactions(description, value, category):
    new_transactions = Transactions(description, value, category)
    CREATE_TRANSACTIONS.append(new_transactions)
    return new_transactions


def total_value():
    total = 0
    for transaction in CREATE_TRANSACTIONS:
        total += transaction.value
    return total
