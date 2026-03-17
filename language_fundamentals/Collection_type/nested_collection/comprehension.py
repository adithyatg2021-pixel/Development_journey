
"""
easy way for creating a sequence from another sequence

list => If we are creating list, it is list comprehension
set => set comprehension
dictionary => dictionary comprehension

syntax: 
list comprehension
[left    middle      right]
return  iteration    condition(if required) 
"""

arr = [10,12,13,14,15]

squares = [num**2 for num in arr] #here using square brackets because it is list comprehension

print(squares)

cubes = [num**3 for num in arr]
print(cubes)

add_10 = [num + 10 for num in arr]
print(add_10)
