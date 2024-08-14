def create_multiplier(x):
    def inner(y):
        return x * y
    return inner


duplicate = create_multiplier(2)
triplicate = create_multiplier(3)

print(duplicate(5))
print(triplicate(5))
