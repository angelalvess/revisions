class Point:
    def __init__(self, x, y, z='sushi'):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}({self.x!r}, {self.y!r}, {self.z!r})'


p1 = Point(1, 2)
p2 = Point(2, 3)
print(p1)
print(p2)
