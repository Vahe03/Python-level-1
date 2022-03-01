# Felix jan yntacqum baner kan tenc el chkareca anem

# 1
class Account:
    _conversion = {'dram': 0.0021, 'euro': 1.12, 'ruble': 0.010, 'dollar': 1}

    def __init__(self, id, name, currency):
        if currency not in Account._conversion.keys():
            raise TypeError

        self._balance = 100
        self.__id = id
        self.__name = name
        self.__currency = currency

    @staticmethod
    def get_meter(x):
        return Account._conversion[x.currency] * x.balance

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self._balance = val

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, val):
        self._balance = val

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, val):
        self._balance = val

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, val):
        self._balance = val

    def credit(self, amount, currency):
        if currency not in Account._conversion:
            raise TypeError
        amount *= Account._conversion.get(currency)
        self._balance += amount
        print('Credit completed')

    def debit(self, amount, currency):
        if currency not in Account._conversion:
            raise TypeError
        amount *= Account._conversion.get(currency)
        if amount > self._balance:
            raise ValueError('Not enough balance')
        else:
            self._balance -= amount
            print('Debit completed')

    def transferTo(self, amount, currency, id):
        if currency not in Account._conversion:
            raise TypeError
        if amount > self._balance:
            raise ValueError('Not enough balance')
        else:
            self._balance -= amount
            print(f'Transfer made to {self.id} account')

    def __str__(self):
        return f'Current balance: {self._balance} dollar'


acc = Account(202299, 'Bill Gates', 'dollar')
print(acc)
acc.credit(100, 'euro')
acc.debit(20, 'dram')
acc.transferTo(50, 'ruble', 29903)
print(acc)


# 2
class SavingsAccount(Account):

    def __init__(self, id, name, currency, interest=10):
        super().__init__(id, name, currency)
        self.interest = interest

    def income(self):
        self._balance = (self._balance * self.interest) / 100
        print("Balance increased")

    def __eq__(self, other):
        if isinstance(other, SavingsAccount):
            self._balance += other._balance


class CurrentAccount(Account):

    def __init__(self, id, name, currency, overdraft_limit=150):
        super().__init__(id, name, currency)
        self.overdraft_limit = overdraft_limit
        self._balance = Account.balance

    def minusValues(self, amount, currency):
        if (self._balance - amount) >= 150:
            self._balance -= amount
            print(f'You have {0 - self._balance} {self.currency} overdraft.')

    def __eq__(self, other):
        if isinstance(other, CurrentAccount):
            self._balance += other._balance


# curAcc = CurrentAccount(14987, 'Elon Musk', 'dollar')
# curAcc.minusValues(20, 'dollar')

# 3
class Person:

    def __init__(self, name, ssn):
        self.name = name
        self.ssn = ssn

    def __str__(self):
        return f'Name: {self.name}'

    def __hash__(self):
        return self.ssn


ssn = Person('Jeff Bezos', 226842)
print(ssn)
print(hash(ssn))


# 4
class Bank:
    _user = {40956: {'Deposit_account_1': 300, 'Savings_account_1': 100}, 56301: {'Deposit_account_2': 70}}

    def __init__(self, ssn, account):
        self.ssn = ssn
        self.account = account
        self._balance = Bank._user.get(ssn).get(account)
        print(self._balance)


bank = Bank(40956, 'Savings_account_1')
