from abc import ABC, abstractmethod


class Account(ABC):

    def __init__(self, agency: int, account_number: int,
                 balance: float) -> None:
        self.agency = agency
        self.account_number = account_number
        self.balance = balance

    @abstractmethod
    def withdraw(self, value: float) -> float:
        pass

    def deposit(self, value: float) -> float:
        self.balance += value
        return self.balance

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}({self.agency}, {self.account_number}, {
            self.balance})'


class CreditAccount(Account):

    def __init__(self, agency: int, account_number: int, balance: float,
                 limit: float):
        super().__init__(agency, account_number, balance)
        self.limit = limit

    def withdraw(self, value):
        available_balance = self.balance + self.limit - value

        if available_balance >= 0:
            self.balance -= value
            print(f'Withdraw of {value} made successfully.')
            print(f'Available balance: {self.balance}')
            return self.balance

        print(f'Insufficient balance. Available balance: {
              self.balance}, limit: {self.limit}')
        return self.balance

    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}({self.agency}, {self.account_number}, {
            self.balance}, {self.limit})'


class SavingAccount(Account):

    def withdraw(self, value):
        available_balance = self.balance - value

        if available_balance >= 0:
            self.balance -= value
            print(f'Withdraw of {value} made successfully.')
            print(f'Available balance: {self.balance}')
            return self.balance

        print(f'Insufficient balance. Available balance: {self.balance}')
        return self.balance


if __name__ == '__main__':
    print('Saving Account')
    saving_account = SavingAccount(1111, 2222, 1000)
    saving_account.deposit(500)
    saving_account.withdraw(2000)
    print()
    print('Credit Account')
    credit_account = CreditAccount(3333, 4444, 1000, 100)
    credit_account.withdraw(1100)
