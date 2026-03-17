
prev = 0
curr = 1
print(prev,curr,end=" ")

for i in range(1,14):
    next = prev + curr
    print(next,end=" ")
    prev = curr
    curr = next
    