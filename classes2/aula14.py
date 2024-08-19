from contextlib import contextmanager


@contextmanager
def my_open(path_file, mode):
    try:
        file = open(path_file, mode)
        yield file
    except Exception as e:
        print(f'Erro: {e}')
    finally:
        print('Fechando arquivo')
        file.close()


with my_open('aula14.txt', 'w') as f:
    f.write('Olá, mundo!', 123)
