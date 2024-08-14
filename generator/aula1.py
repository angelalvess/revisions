
# entrega um valor por vez, diferente de
# uma lista que entrega todos os valores de uma vez

generator = (n for n in range(1000))

print(generator)
print(next(generator))
print(next(generator))
