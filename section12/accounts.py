import datetime
import pytz


class Account:
    """ simple account class with balnace """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

# obj._var = protected variable
# obj.__var = private variable
# obj.__var__
    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = [(Account._current_time(), balance)] # inital input
        print("Acount created for " + self._name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance-=amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than zero and more than your account balence")
            self.show_balance()
    
    def show_balance(self):
        print("balance is {}".format(self.__balance))
        

    def show_transaction(self):
        for date, amount in self._transaction_list:
            if amount > 0:                
                tran_type = "deposited"
            else:
                tran_type = "withdraw"
                amount*=-1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))


if __name__ == "__main__":
    tim = Account("victor", 0)
    tim.show_balance()
    tim.deposit(1000)
    #tim.show__balance()
    tim.withdraw(500)
    #tim.show__balance()

    tim.withdraw(2000)

    tim.show_transaction()
    tim.show_balance()
    #print(type(Account._current_time()))
    #print(Account._current_time().astimezone())

    steph = Account("steph", 800)
    steph.__balance = 20
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transaction()
    steph.show_balance()
    print(steph.__dict__)






        
