letras = set()

while True:
    letra = input('Digite uma letra: ')
    if letra == '':
        break
    letras.add(letra.lower())
    print(letras)
