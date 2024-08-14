lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

l1 = sorted(lista, key=lambda x: x['nome'])
l2 = sorted(lista, key=lambda x: x['sobrenome'])


def show(lista):
    for item in lista:
        print(item)


show(l1)
print()
show(l2)
print()
