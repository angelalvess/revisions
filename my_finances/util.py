from category import Category
from transactions import Transactions

LIST_CATEGORIES = []
LIST_TRANSACTIONS = []


def create_category(name):
    category = Category(name=name)
    LIST_CATEGORIES.append(category)
    return category


def create_transactions(description, value, category):
    transactions = Transactions(
        description=description, value=value, category=category)

    LIST_TRANSACTIONS.append(transactions)
    return transactions


def total_value():
    total = 0
    for transactions in LIST_TRANSACTIONS:
        total += transactions.value
    return total
