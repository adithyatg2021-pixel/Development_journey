from copy import deepcopy

lst = [[1,2],[3,4],[5,6]]

lst1 = lst.copy()
lst1[1][1] = 10
print("Shallow copy")
print(lst)
print(lst1)

lst2 = [[1,2],[3,4],[5,6]]
lst3 = deepcopy(lst2)
lst3[1][1] = 10
print("Deep copy")
print(lst2)
print(lst3)



