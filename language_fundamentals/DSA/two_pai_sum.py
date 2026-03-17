
arr = [2,3,4,5]

sum = 8

# for n in arr:
#     for num in arr:
#         if n + num == sum:
#             print(f"({n},{num})")
           
arr.sort()
left = 0
right = len(arr) - 1

while left < right:
    current_sum = arr[left] + arr[right]
    if current_sum == sum:
        print(f"{arr[left]},{arr[right]}")
        break
    elif current_sum < sum:
        left += 1
    elif current_sum > sum:
        right -= right