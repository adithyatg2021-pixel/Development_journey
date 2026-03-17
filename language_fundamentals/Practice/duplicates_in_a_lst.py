lst = [10,11,11,12,13,10,14,15,16,14,18,30]

# st = set()

# for num in lst:
#     if lst.count(num) > 1:
#         st.add(num)

# print(st)


lst.sort()

curr = 0
next = curr + 1

for i in range(0,len(lst)-1):
    if lst[curr] == lst[next]:
        print(lst[curr])
        curr += 1
        next = curr + 1
    else:
        curr += 1
        next = curr + 1

