
age = {"Manu":25,"Siva":21,"Preethi":26,"Keerth":20}

highest_age = 0

for k, v in age.items():
    if v > highest_age:
        highest_age = v
        name = k
print(name,highest_age)