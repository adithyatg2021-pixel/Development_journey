
num = int(input("Enter the number to search:"))

present = 0

num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,34,42,45,78,67,0,85,102]

for number in num_list:
    if num == number:
        present = 1
if present == 1:
    print("Searched element present in list.")
else:
    print("Searched element not present in list.")
    