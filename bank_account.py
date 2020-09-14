class BankAccount():
    def __init__(self, kind):
        self.kind = kind
        self.balance = 0
        self.overdraft_fees = 0
        self.pin = pin

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount, pin_from_user):

        if (self.pin == pin_from_user):

            if (self.balance < amount):
                print("Insuficient funds")
                return
            elif (self.balance == amount):
                self.balance -= amount
                print("current balance is now {}".format(self.balance))
            else: 
                self.balance -= amount
                print("current balance is now {}".format(self.balance))

        self.balance -= amount

        if(self.balance < 0):
            self.overdraft_fees += 36
        return amount
    
    def change_pin(self, pin):
        self.pin = pin
        print(f"The new pin number is {self.pin}")
    
shane_checking = BankAccount("checking", 1234)
print("My new account is a {} account".format(shane_checking.kind))

shane_checking.deposit(2000)
print("My current balance is ${}.".format.(shane_checking.balance))

shane_checking.withdraw(1000)
print("My current balance is ${}.".format.(shane_checking.balance))

shane_checking.withdraw(2000)
print("My current balance is ${}.".format.(shane_checking.overdraft_fees))

shane_checking