def execute_function(func, *args):
    return func(*args)


def summ(x, y):
    return x + y


print(execute_function(summ, 10, 20))
