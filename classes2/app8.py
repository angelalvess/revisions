class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection


c1 = Connection()
c1.set_user('root')
c1.set_password('123456')
print(c1.user, c1.password)

c2 = Connection.create_with_auth('random', '456')
print(c2.user, c2.password)
