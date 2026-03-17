lst = [1,2,3,4,5,6,7,8]

sum = 6

l = 0
r= len(lst) - 1

for i in range(0,len(lst)):
    if lst[l] + lst[r] == sum:
        print(f"({lst[l]},{lst[r]})")
        l += 1
        r += 1
    elif lst[l] + lst[r] < sum:
        l += 1
    else:
        r -= 1