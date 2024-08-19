class MyContextManager:

    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.file = None

    def __enter__(self):
        print('Entrando no contexto')
        self.file = open(self.path, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        print('Saindo do contexto')
        self.file.close()


with MyContextManager('aula13.txt', 'w') as f:
    f.write('Olá, mundo!')
