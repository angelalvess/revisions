class FavFood:
    def __init__(self, name):
        self.name = name

    def favorite_food(self, food):
        return f'{self.name} favorite food is {food}'

    def sushi(self, *args, **kwargs):
        return self.favorite_food(*args, **kwargs)

    @property
    def name(self):
        return self._name.title()

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError('Name must be a string')
        self._name = value


angel = FavFood('angel')
print(angel.favorite_food('Pizza'))
print(angel.sushi('Sushi'))
