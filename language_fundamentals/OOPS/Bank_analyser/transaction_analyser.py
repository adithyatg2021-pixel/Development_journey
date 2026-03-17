from csv import DictReader

class TransactionAnalyser:

    def __init__(self):
        fr = open("language_fundamentals\\OOPS\\Bank_analyser\\bank_transactions_500_records.csv")
        self.transactions = list(DictReader(fr))

    def debit_transactions(self):
        print("DEBIT TRANSACTIONS")
        for t in self.transactions:
            if t.get("type") == "debit":
                print(t)
        print("\n")

    def credit_transactions(self):
        print("CEBIT TRANSACTIONS")
        for t in self.transactions:
            if t.get("type") == "credit":
                print(t)
        print("\n")

# high value transaction, highest debit transaction, highest credit transaction

    def high_value_transaction(self):
        print("HIGH VALUE TRANSACTIONS")
        for t in self.transactions:
            if t.get("amount") > 75000:
                print(t)
        print("\n")

    def high_credit_transaction(self):
        print("HIGH CREDIT TRANSACTION")
        high_credit = max([t.get("amount") for t in self.transactions if t.get("type") == "credit"])
        print(high_credit)
        print("\n")

    
    def high_debit_transaction(self):
        print("HIGH DEBIT TRANSACTION")
        high_debit = max([t.get("amount") for t in self.transactions if t.get("type") == "debit"])
        print(high_debit)
        print("\n")


trans_instance = TransactionAnalyser()
trans_instance.debit_transactions()
trans_instance.credit_transactions()
trans_instance.high_credit_transaction()
trans_instance.high_debit_transaction()