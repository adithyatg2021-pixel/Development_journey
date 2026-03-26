from copy import deepcopy
lst = [[0,0],[0,1],[1,1],[1,3]]
print("Using shallow copy")
lst1 = lst.copy()
lst1[3][1] = 2
print("List 1:",lst)
print("List 2:",lst1)

lst2 = [[0,0],[0,1],[1,1],[1,3]]
print("Using deep copy")
lst3 = deepcopy(lst2)
lst3[3][1] = 2
print("List 1:",lst2)
print("List 2:",lst3)