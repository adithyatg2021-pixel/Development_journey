principal_amount = 50000
rate = 5
n = 4
emi = (principal_amount * rate * ((1 + rate) ** n))/ (((1 + rate) ** n) - 1)
print("EMI:",emi)