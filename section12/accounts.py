import datetime
import pytz

class Account:
    """ simple account class with balnace """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print("Acount created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_list.append((pytz.utc.localize(datetime.datetime.utcnow(), amount)))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance-=amount
        else:
            print("The amount must be greater than zero and more than your account balence")
            self.show_balance()
    
    def show_balance(self):
        print("balance is {}".format(self.balance))
        

    def show_transaction(self):
        for date, amount in self.transaction_list:
            if amount > 0:                
                tran_type = "deposited"
            else:
                tran_type = "withdraw"
                amount*=-1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == "__main__":
    tim = Account("victor", 2)
    tim.show_balance()

    tim.deposit(100)
    tim.show_balance()
    tim.withdraw(500)
    tim.show_balance()




        
