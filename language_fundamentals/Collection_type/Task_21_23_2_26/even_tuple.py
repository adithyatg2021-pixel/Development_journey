
tup = (34,13,90,67,55,83)

lis = []

for i in range(0,len(tup)):
    if tup[i] % 2 == 0:
        lis.append(tup[i])

even_tup = tuple(lis)

print("Tuple with even elements:",even_tup)