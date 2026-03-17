
number_list = [4676,42,1789,786,78567]

largest = 0

for i in range(0,len(number_list)):
    if number_list[i] > largest:
        largest = number_list[i]

print("Largest element in list:",largest)
