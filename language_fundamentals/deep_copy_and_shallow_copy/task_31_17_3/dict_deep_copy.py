from copy import deepcopy
dictionary = {0:[1,2],1:[3,4]}
dictionary1 = deepcopy(dictionary)

dictionary1[0] = [5,6]

print("First dict:",dictionary)
print("Second dict:",dictionary1)

