
list1 = [10,11,12,13,14,8]

list2 = [8,11,14,15,16]

# Method 1

# for i in range(0,len(list1)):
#     for j in range(0,len(list2)):
#         if list1[i] == list2[j]:
#             print(list1[i])

# Method 2

# for num in list1:
#     if num in list2:
#         print(num)

# Method 3

# list1.extend(list2)
# list1.sort()
# for prev in range(0,len(list1)-1):
#     next = prev + 1
#     difference  = list1[next] - list1[prev]
#     if difference == 0:
#         print(list1[prev])

# Method 4

# st1 = set(list1)
# st2 = set(list2)

# common_elements = st1.intersection(st2)

# print(common_elements)

# Method 5

list1.sort()
list2.sort()

p1 = 0
p2 = 0

while(p1 < len(list1) and p2 < len(list2)):

    if list1[p1] == list2[p2]:
        print(list1[p1])
        p1 += 1
        p2 += 1
    elif list1[p1] < list2[p2]:
        p1 += 1
    else:
        p2 += 1