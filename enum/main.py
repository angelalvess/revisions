import enum


class Direction(enum.Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


def move(direction: Direction):

    if not isinstance(direction, Direction):
        raise ValueError('Invalid direction')

    return f'Moving {direction.name.lower()}'


print(move(Direction.UP))
