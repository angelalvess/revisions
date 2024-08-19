class MyError(Exception):
    pass


def test():
    raise MyError('My error message')


test()
