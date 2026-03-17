
"""
Create a dictionary:
account_number
holder_name
balance
Tasks:
Deposit 5000
Withdraw 2000
Check if balance is less than 1000 → print "Low Balance"

"""
bank_acc_det = {"Account_number":6787950,"Holder_name":"Deepika","Balance":1000}

# Deposite 5000

bank_acc_det["Balance"] += 5000

print(bank_acc_det)

# Withdraw 2000

if bank_acc_det["Balance"] > 2000:

    bank_acc_det["Balance"] -= 2000

else:
    
    print("Insufficient balance amount to withdraw.")

print(bank_acc_det)

if bank_acc_det["Balance"] < 1000:

    print("Low Balance")