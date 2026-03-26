from functools import reduce

lst = [1,2,3,4,5]

res = reduce(lambda n1,n2 : n1 * n2,lst)
print(res)