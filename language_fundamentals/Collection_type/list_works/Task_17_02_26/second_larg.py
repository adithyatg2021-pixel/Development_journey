
num_list = [78,245,157,90,134,186,196]

largest = 0
second_largest = 0

for num in num_list:
    if num > largest:
        if num > second_largest:
            second_largest = largest
            largest = num
    else:
        if num > second_largest:
            second_largest = num

print("Second largest element in list:",second_largest)

