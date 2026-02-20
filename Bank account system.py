class BankAccount:
    
    
    def __init__(self, holder_name, account_number, balance):
        self.holder_name = holder_name
        self.account_number = account_number
        self.balance = balance

    
    def deposit(self, amount):
        self.balance += amount
        print("Deposited Amount:", amount)

    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            print("Withdrawn Amount:", amount)

    
    def display_balance(self):
        print("\nAccount Holder Name:", self.holder_name)
        print("Account Number:", self.account_number)
        print("Current Balance:", self.balance)



account1 = BankAccount("Vinayak", 1234567890, 5000)

# Calling methods
account1.display_balance()
account1.deposit(2000)
account1.withdraw(1500)
account1.display_balance()
