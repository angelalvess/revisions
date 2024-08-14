class Cliente:
    def __init__(self, name, mail, plan):
        self.name = name
        self.mail = mail
        self.plans = ['free', 'premium', 'enterprise']
        if plan in self.plans:
            self.plan = plan

    def change_plan(self, new_plan):
        if new_plan in self.plans:
            self.plan = new_plan
            print('Plano alterado com sucesso! Seu novo plano é:'
                  ' {}'.format(self.plan))
        else:
            raise ValueError('Plano inválido!')

    def watch_movies(self, movie, plan_movie):
        if self.plan == plan_movie:
            print('Assistir filme: {}'.format(movie))
        elif self.plan == 'premium' or self.plan == 'enterprise':
            print('Assistir filme: {}'.format(movie))
        elif self.plan == 'free' and plan_movie == 'premium':
            print('Assine um plano premium para assistir este filme!')
        else:
            print('Plano invalido!')

    def watch_series(self, serie, plan_serie):
        if self.plan == plan_serie:
            print('Assistir série: {}'.format(serie))
        elif self.plan == 'premium' or self.plan == 'enterprise':
            print('Assistir série: {}'.format(serie))
        elif self.plan == 'free' and plan_serie == 'premium':
            print('Assine um plano premium para assistir esta série!')
        else:
            print('Plano invalido!')


cliente = Cliente('angel', 'angel@gmail.com', 'free')
cliente.watch_movies('Titanic', 'premium')
cliente.watch_series('Friends', 'premium')
cliente.change_plan('enterprise')
cliente.change_plan('free')
