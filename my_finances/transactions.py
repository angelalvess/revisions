from dataclasses import dataclass
from category import Category


@dataclass
class Transactions:
    description: str
    value: float
    category: Category

    def show(self):
        print(f'{self.description} - {self.value} - {self.category.name}')
