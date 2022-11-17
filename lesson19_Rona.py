class Account:
    def __init__(self, balance, account_number):
        self._balance = balance
        self._account_number = account_number

    @classmethod
    def create_account(cls, account_number):
        return cls(0.0, account_number)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

    def __str__(self):
        return f'Account number: {self._account_number}, balance: {self._balance}'


class SavingsAccount(Account):
    def __init__(self, balance, account_number):
        super().__init__(balance, account_number)
        self.interest = 0

    def interest_update(self):
        self.interest += 1


class CurrentAccount(Account):
    def __init__(self, balance, account_number):
        super().__init__(balance, account_number)
        self.overdraft = 50


# b.2
class Bank:
    def __init__(self, bank_account: list[Account]):
        self.bank_account = bank_account

    def open_account(self, number):
        new_acc = Account.create_account(account_number=number)
        new_acc.deposit(500)
        self.bank_account.append(new_acc)

    def close_account(self, account):
        self.bank_account.remove(account)

    # b.3
    def update(self):
        for i in self.bank_account:
            if isinstance(i, SavingsAccount):
                i.interest_update
            elif isinstance(i, CurrentAccount):
                if i.overdraft > i.get_balance():
                    print('Send the letter: "overdraft')