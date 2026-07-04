class MyBank:
    def __init__(self,balance,accountNo):
        self.balance=balance
        self.accountNo=accountNo
        self.history=[]

    def withdraw(self,amount):
        if(self.balance>0 and self.balance >= amount):
                self.balance=self.balance-amount
                self.transactionHistory("Debited", amount)
                return self.balance
    def deposit(self,amount):
        if(amount>0):
            self.balance=self.balance+amount
            self.transactionHistory("deposit", amount)
            return self.balance
    def check_balance(self):
        return self.balance
    def check_history(self):
        return self.history
    def transactionHistory(self, transaction_type, amount):
        self.history.append((transaction_type, amount))
        return self.history
    def transfer(self,amount, anotherAccount):
        self.withdraw(amount)
        anotherAccount.deposit(amount)
        return anotherAccount.balance






myBank1=MyBank(2000,123432)
# myBank1.withdraw(1000)
myBank1.deposit(2000)
# print(myBank1.check_history())


myBank2=MyBank(23000,123433)
# withdraw=myBank2.withdraw(100)
myBank2.deposit(2000)
myBank1.transfer(500,myBank2)
print(myBank1.check_balance())
print(myBank2.check_balance())
print(myBank1.check_history())
print(myBank2.check_history())
