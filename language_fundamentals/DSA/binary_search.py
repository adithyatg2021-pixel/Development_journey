"""
Algorith:
1. sort array
2. Set low = 0
3. Set high = len(arr) - 1
4. loop low <= high
        mid = (low + high) // 2
        case 1: element == arr[mid] : element found, break
        case 2: element < arr[mid]  : upp = mid - 1
        case 3 : element > arr[mid] : low = mid + 1
"""


arr = [23,34,12,78,10,15,67,1,10,17]
element = int(input("Enter element to search:"))
arr.sort()
low = 0
upp = len(arr) - 1
is_present = False

while(low <= upp):

    mid = (low + upp) // 2

    if arr[mid] == element:
        is_present = True
        break
    elif element < arr[mid]:
        upp = mid - 1
    elif element > arr[mid]:
        low = mid + 1

print(is_present)
        