
set1 = {23,78,12,89,34}
set2 = {11,90,89,34,15,32}
set3 = {89,34,77,56,15,32}

print("Set1:",set1)
print("Set2:",set2)
print("Set3:",set3)

set4 = set1.intersection(set2)
set5 = set4.intersection(set3)

print("Common elements in 3 sets:",set5)
