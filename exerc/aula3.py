
def greeting(name, age):
    return f"Hello {name}, you are {age} years old."


def multply(a, b):
    return a * b


def create_function(func, a):
    def inner(b):
        return func(a, b)
    return inner


multiply_by_2 = create_function(multply, 2)
greeting_john = create_function(greeting, "John")

print(multiply_by_2(3))
print(greeting_john(25))
