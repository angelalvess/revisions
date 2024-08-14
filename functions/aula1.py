def soma(num1, num2):
    return num1 + num2


def subtrair(num1, num2):
    return num1 - num2


def mat(num1, num2, func=soma):
    return func(num1, num2)


print(mat(2, 3, subtrair))
print(mat(2, 3))


def soma_args(*args):
    return sum(args)


numbers = [1, 2, 3, 4, 5]

print(soma_args(*numbers))
