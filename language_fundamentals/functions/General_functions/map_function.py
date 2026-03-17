
"""
to perform a functionality over the objects of a collection

"""
lst = [1,2,3,4,5]

map_square = list(map(lambda n:n**2,lst))
print(map_square)

comp_square = [num**2 for num in lst]
print(comp_square)

map_cube = list(map(lambda n:n**3,lst))
print(map_cube)

comp_cube = [num**3 for num in lst]
print(comp_cube)