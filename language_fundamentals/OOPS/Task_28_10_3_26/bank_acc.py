class BankAccount:

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def display(self):
        print(f"Account holder name: {self.name}")
        print(f"Balance: {self.balance}")

bank1 = BankAccount("Athira",120000)
bank1.display()
    