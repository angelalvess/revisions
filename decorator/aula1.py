def validate_sum(func):

    def inner(x, y):
        if x < 0 or y < 0:
            raise ValueError('Only positive numbers are allowed')
        return func(x, y)
    return inner


@validate_sum
def summ(x, y):
    return x + y


print(summ(-1, 2))
