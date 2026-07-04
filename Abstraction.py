class MyBank:
    def __init__(self,balance,accountNo):
        self.balance=balance
        self.accountNo=accountNo
    def debit_money(self,amount):
        if(self.balance>0 and self.balance > amount):
            self.balance=self.balance-amount
            print("amount debited->",amount,",remaining balance after debit:",self.balance_check())
    def credit_money(self,amount):
        if(amount>0):
            self.balance=self.balance+amount
            print("amount credited->",amount,",after money credited balance is:",self.balance_check())
    def balance_check(self):
        return self.balance
    
openAcc=MyBank(2000,123432)
openAcc.debit_money(100)
openAcc.credit_money(2000)
print(openAcc.balance_check())






# class Car:
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.clutch=False
#     def start(self):
#         self.clutch=True
#         self.brk=True
#         self.acc=True
#         print("bike started")

# c=Car()
# c.start()