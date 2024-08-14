prices = [10, 20, 30]


def filter_prices(price):
    if price > 15:
        return True

    return False


new_prices = list(filter(filter_prices, prices))
print(new_prices)
