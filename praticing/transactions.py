from category import Category
from dataclasses import dataclass


@dataclass
class Transactions:
    description: str
    value: float
    category: Category

    def show(self):
        print(f'Description: {self.description} | Value: {
              self.value} | Category: {self.category.name}')
