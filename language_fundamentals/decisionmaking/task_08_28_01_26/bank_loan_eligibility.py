income = int(input("Enter monthly income:"))

if income >= 25000:
    credit_score = int(input("Enter credit score:"))
    if credit_score >= 700:
        print("Loan approved")
    else:
        print("Low credit score")
else:
    print("Income not sufficient")