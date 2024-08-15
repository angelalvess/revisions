

# Closure sem chamar a func na inner
def intro(name):
    def inner(age):
        return f"Hello {name}, you are {age} years old."
    return inner


def summation(a, b):
    return a + b


def outer(func, a):
    def inner(b):
        return func(a, b)
    return inner


intro1 = intro("John")
print(intro1(25))

summation1 = outer(summation, 10)
print(summation1(20))
