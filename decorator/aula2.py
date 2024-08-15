# validar os paramentros


def validate_summ(func):
    def inner(x, y):
        if x < 0 or y < 0:
            raise ValueError('Only positive numbers are allowedd')
        return func(x, y)
    return inner


@validate_summ
def summ(x, y):
    return x + y


s1 = summ(1, 2)
print(s1)
s2 = summ(-1, 2)
print(s2)
