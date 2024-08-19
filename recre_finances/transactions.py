from dataclasses import dataclass
from categories import Category


@dataclass
class Transaction:
    description: str
    value: float
    category: Category

    def show(self):
        print(f'Description: {self.description}, Value: {
              self.value}, Category: {self.category.name}')
