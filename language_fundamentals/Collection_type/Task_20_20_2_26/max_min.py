
tup = (24,89,56,178,36)

max = 0
min = tup[0]

for e in tup:
    if e > max:
        max = e
    if e < min:
        min = e
print("Maximum element:",max)
print("Minimum element:",min)