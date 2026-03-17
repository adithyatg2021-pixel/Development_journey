pin = 4589
balance = 30000

user_pin = int(input("Enter PIN:"))

if user_pin == pin:
    withdrawal_amount = int(input("Enter withdrawal amount:"))
    if withdrawal_amount <= balance:
        print("Withdrawal successful")
    else:
        print("Insufficient balance")
else:
    print("Incorrect PIN")