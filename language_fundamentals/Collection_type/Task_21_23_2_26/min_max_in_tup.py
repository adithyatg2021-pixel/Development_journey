
tup = (23,67,3,90,154,89)

max = 0
min = tup[0]

for i in range(0,len(tup)):
    if tup[i] > max:
        max = tup[i]
    if tup[i] < min:
        min = tup[i]

print("Max value:",max)
print("Min value:",min)