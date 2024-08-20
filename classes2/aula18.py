class Multiply:
    def __init__(self, func):
        self.func = func
        self.duplication = 2

    def __call__(self, *args, **kwargs):
        print(args, kwargs)
        result = self.func(*args, **kwargs)
        return result * self.duplication


@Multiply
def summation(a, b):
    return a + b


s1 = summation(1, 2)
print(s1)
