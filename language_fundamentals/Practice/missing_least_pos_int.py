lst = [2,4,1,5]

lst.sort()

curr = 0
next = curr+1

for i in range(0,len(lst)-1):

    if lst[curr] + 1 == lst[next]:
        curr += 1
        next = curr + 1
    else:
        print(next+1,"is missing")
        break
else:
    print(lst[-1]+1,"is missing")