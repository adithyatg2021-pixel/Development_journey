number_list = [287,1688,67,2378,12906,789]

smallest = number_list[0]

for num in number_list:
    if num < smallest:
        smallest = num

print("Smallest number in the list:",smallest)