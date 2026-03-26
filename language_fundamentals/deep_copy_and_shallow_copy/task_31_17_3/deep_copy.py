from copy import deepcopy

lst = [[0,0],[0,1],[1,1],[1,3]]

lst1 = deepcopy(lst)
lst1[3][1] = 2
print("List 1:",lst)
print("List 2:",lst1)