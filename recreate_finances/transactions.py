from dataclasses import dataclass
from category import Category


@dataclass
class Transactions:
    description: str
    value: float
    category: Category

    def show(self):
        print(f'Description: {self.description} | Value: {
            self.value} | Category: {self.category.name}')
