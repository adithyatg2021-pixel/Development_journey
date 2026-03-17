lst = [1,2,3,4,5,6]

print(lst[3:])

lst.append(7)
lst.insert(7,8)
lst.pop()
lst.pop(6)
lst.remove(6)
print(lst.count(4))
lst.sort()
lst.sort(reverse=True)
lst2 = [6,7,8,9]
lst.extend(lst2)
lst.clear()
print(lst)