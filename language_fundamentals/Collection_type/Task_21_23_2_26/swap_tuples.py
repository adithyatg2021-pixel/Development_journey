
tup1 = (12,45,89,45)
tup2 = (34,90,1,67)
print("Tuple 1 and 2 before swapping:")
print("Tuple1:",tup1)
print("Tuple2:",tup2)
li1 = list(tup1)
li2 = list(tup2)
temp = 0
i = 0
while(i < len(li1) and len(li2)):
    temp = li1[i]
    li1[i] = li2[i]
    li2[i] = temp
    i +=1
tup1 = tuple(li1)
tup2 = tuple(li2)
print("Tuple 1 and 2 after swapping:")
print(tup1)
print(tup2)


