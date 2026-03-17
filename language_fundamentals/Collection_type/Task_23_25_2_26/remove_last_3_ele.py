
lst = [34,12,78,56,10,89,77,1,16,45]

lst1 = lst[-3:]

for v in lst1:
    lst.remove(v)

print(lst)