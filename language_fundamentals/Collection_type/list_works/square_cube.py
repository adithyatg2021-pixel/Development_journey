"""
w.a.p to create 2 list squares_list and cube_list

"""

numbers = [2,3,4,5,6,12,13]

squares_list = []
cube_list = []

for num in numbers:
    sq = num ** 2
    squares_list.append(sq)

    cube = num ** 3
    cube_list.append(cube)

print("Square list",squares_list)
print("Cube list",cube_list)