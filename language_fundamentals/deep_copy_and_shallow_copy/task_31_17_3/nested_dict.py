from copy import deepcopy

lst = [{"name":"Keerthy","age":20},{"Subject":"Python","marks":89}]

lst1 = deepcopy(lst)

lst1[1]["marks"] = 90

print(lst)
print(lst1)


