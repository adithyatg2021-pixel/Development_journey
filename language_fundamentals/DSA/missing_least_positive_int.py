
"""
w.a.p to display least positive missing integer from list with +ve numbers

sample input1:
    lst=[1,2,3,5]

    o/p => 4

sample input2:
    lst=[2,3,4,5]

    o/p => 1

sample input3:
    lst=[1,2,3,4,5]
    o/p=>6
"""

lis = [1,2,3,5]

# length = len(lis)

# for i in range(1,length+1):         # if the for loop worked without break, then the else of for will work
#     if i not in lis:
#         print(i,"is missing")
#         break
# else:
#     print(length+1,"is missing")

lis.sort()

prev = 0
next = prev+1

for prev in range(0,len(lis)-1):
    difference = lis[next] - lis[prev]
    if difference != 1:
        print(lis[prev]+1,"is missing.")
    
    prev = prev+1
    next = prev+1

else:
    print(lis[-1]+1,"is missing.")


# def missing_positive_int(arr):
#     arr.sort()

#     prev= 0
#     next = prev+1

#     while(prev <= len(arr)-1):
#         difference = arr[next] - arr[prev]
#         if difference != 1:
#             print(arr[prev]+1,"is missing.")
#             break
#         prev += 1
#         next = prev+1

# missing_positive_int(lis)