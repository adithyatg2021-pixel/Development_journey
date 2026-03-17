
manali = {
    "Dijo":300,
    "Akshay":1000,
    "Edwin":800,
    "Alan":15000,
    "Manoj":0,
    "Subin":0,
    "Sreeyesh":500
}

total_expense = 0

for v in manali.values():
    total_expense += v

print("Total expense:",total_expense)

individual_split = round(total_expense/len(manali))

print("Individual split:",individual_split)

# new dict with balance payments

spend_wise = {}

for k,v in manali.items():

    payment = individual_split - v

    spend_wise[k] = payment

print("Dict with balance payments:",spend_wise)