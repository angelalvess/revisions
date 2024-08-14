class ControleRemote:
    def __init__(self, color):
        self.color = color

    def passar_canal(self, botao):
        if botao == 'up':
            print('Canal aumentado')
        elif botao == 'down':
            print('Canal diminuido')


controle_sala = ControleRemote('preto')
print(controle_sala.color)
controle_sala.passar_canal('up')

controle_quarto = ControleRemote('branco')
print(controle_quarto.color)
controle_quarto.passar_canal('down')
