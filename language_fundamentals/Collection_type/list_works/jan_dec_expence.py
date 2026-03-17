
exp = [12000,11600,15000,14890,17889,9567,19674,17548,13900,14680,16300,10680]

total_expense = 0
for ex in exp:
    total_expense += ex

print("Total expense:",total_expense)
print("Average expense:",total_expense/len(exp))
