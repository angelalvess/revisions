from category import Category
from transactions import Transactions


LIST_CATEGORIES = []
LIST_TRANSACTIONS = []


def create_category(name):
    new_category = Category(name=name)
    LIST_CATEGORIES.append(new_category)
    return new_category


def create_transactions(description, value, category):
    new_transaction = Transactions(
        description=description, value=value, category=category)
    LIST_TRANSACTIONS.append(new_transaction)
    return new_transaction


def total_value():
    total = 0

    for transaction in LIST_TRANSACTIONS:
        total += transaction.value
    return total


print(LIST_CATEGORIES)
print(LIST_TRANSACTIONS)
