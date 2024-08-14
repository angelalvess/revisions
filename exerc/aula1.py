perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opcoes': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opcoes': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opcoes': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opcoes']
    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')

    choice = input('Escolha uma opção: ')

    acertou = False
    choice_int = None
    qtd_choices = len(opcoes)

    if choice.isdigit():
        choice_int = int(choice)

    if choice_int is not None:
        if choice_int >= 0 and choice_int < qtd_choices:
            if opcoes[choice_int] == pergunta['Resposta']:
                acertou = True

    if acertou:
        qtd_acertos += 1
        print('Você acertou!')
    else:
        print('Você errou!')

print(f'Você acertou {qtd_acertos} de {len(perguntas)} perguntas.')
