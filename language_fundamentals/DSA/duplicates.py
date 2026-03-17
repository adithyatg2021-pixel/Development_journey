
"""
Find the duplicate elements in the list without using buil-in methods
"""

# def duplicate_elements(arr):

#     arr.sort()

#     prev = 0
#     next = prev+1

#     for prev in range(0,len(arr)-1):
#         difference = arr[next] - arr[prev]

#         if difference == 0:
#             print(arr[prev])


lst = [10,11,12,11,13,14,15,13]

st = set()

# duplicate_elements(lst)

for i in range(0,len(lst)):
    for j in range(0,len(lst)):
        if i != j:
            if lst[i] == lst[j]:
                st.add(lst[i])
for n in st:
    print(n)