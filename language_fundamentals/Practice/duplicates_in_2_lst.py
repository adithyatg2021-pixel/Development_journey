lst1 = [10,55,23,90]

lst2 = [1,7,10,90,55]

lst1.sort()
lst2.sort()

p1 = 0
p2 = 0

while(p1 < len(lst1) and p2 < len(lst2)):

    if lst1[p1] == lst2[p2]:
        print(lst2[p2])
        p1 += 1
        p2 += 1

    elif lst1[p1] <lst2[p2]:
        p1 += 1
    else:
        p2 += 1