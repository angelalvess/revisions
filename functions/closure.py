def create_greeting(greet):
    def inner(name):
        return f'{greet}, {name}!'
    return inner


greet = create_greeting('Morning')


print(greet('John'))
