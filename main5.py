class account:
    def __init__(self):
        self.balance=0
        print("new account created")
    def deposit(self):
        amount=float(input("enter amount to deposit: "))
        self.balance+=amount
        print('new balance:%f' %self.balance)
    def withdraw(self):
        amount=float(input("enter amount to withdraw: "))
        if(amount>self.balance):
            print("insufficient balance")
        else:
            self.balance-=amount
            print('new balance: %f' %self.balance)
    def enquiry(self):
        print('balance:%f' %self.balance)
account=account()
account.deposit()
account.withdraw()
account.enquiry()