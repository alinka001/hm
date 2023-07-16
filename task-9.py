class BankAccount :
    def __init__(self, balance, interest_rate) :
        self.balance = balance
        self.interest_rate = interest_rate

    def deposit(self, value) :
        self.balance += value

    def withdraw(self, value):
        self.balance -= value

    def add_interest(self, multiplier) :
        self.balance += self.balance / 100 * multiplier

    def is_negative(self):
        if self.balance < 0 :
            return True
        else :
            return False
        

bank_account = BankAccount(100, 5)
bank_account.deposit(50)
print(bank_account.balance)
bank_account.withdraw(50)
print(bank_account.balance)
bank_account.add_interest(20)
print(bank_account.balance)
print(bank_account.is_negative())