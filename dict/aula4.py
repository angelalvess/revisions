pessoa = {
    'nome': 'João',
    'sobrenome': 'Moreira',
}

dados = {
    'cidade': 'Belo Horizonte',
    'estado': 'Minas Gerais',
}

pessoa_completa = {**pessoa, **dados}

print(pessoa_completa)
