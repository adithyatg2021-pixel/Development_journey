class Payment:
    def pay(self): pass

class CreditCard(Payment):
    def pay(self):
        print("Credit card payment")

class UPI(Payment):
    def pay(self):
        print("UPI Payment")

crecar_inst = CreditCard()
crecar_inst.pay()

upi_inst = UPI()
upi_inst.pay()