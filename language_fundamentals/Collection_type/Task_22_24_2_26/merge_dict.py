
dic1 = {"Name":"Sona","Age":23}

print("D1:",dic1)

dic2 = {"Course":"Python","Fee":55000}

print("D2:",dic2)


for k,v in dic2.items():
    dic1[k] = v
print("Merged list:",dic1)