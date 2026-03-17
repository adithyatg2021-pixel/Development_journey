
"""
used to filter the objects in a collection based on a condition
"""

lst = [11,12,13,14,15,16]

even_filter = list(filter(lambda n:n%2==0,lst))
print(even_filter)

even_comp = [num for num in lst if num % 2 == 0]
print(even_comp)

odd_filter = list(filter(lambda n:n%2 != 0,lst))
print(odd_filter)

odd_comp = [num for num in lst if num % 2 != 0]
print(odd_comp)
