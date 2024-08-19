from transactions import Transaction
from categories import Category


list_categories = []
list_transactions = []


def add_category(name):
    new_category = Category(name)
    list_categories.append(new_category)
    return new_category


def add_transaction(description, value, category):
    new_transaction = Transaction(description, value, category)
    list_transactions.append(new_transaction)
    return new_transaction


def total():
    total = 0
    for transaction in list_transactions:
        total += transaction.value
    return total
