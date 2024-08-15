def by_zero(func):
    def inner(x, y):
        if x == 0 or y == 0:
            raise ValueError('Zero is not allowed')
        return func(x, y)
    return inner


@by_zero
def multiply(x, y):
    return x * y


m1 = multiply(1, 2)
print(m1)

m2 = multiply(0, 2)
print(m2)
