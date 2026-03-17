amount = int(input("Enter amount:"))

if amount > 5000:
    print("20 % discount")
    print("Final price:",amount * (20/100))
elif amount >= 2000:
    print("10 % discount")
    print("Final price:",amount * (10/100))
else:
    print("No discount below purchase amount 2000.")
    