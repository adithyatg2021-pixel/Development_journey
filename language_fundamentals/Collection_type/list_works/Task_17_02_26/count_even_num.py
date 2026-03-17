
number_list = [35,789,64,128,895,164,34,876,342,17]

count = 0

for num in number_list:
    if num % 2 == 0:
        count += 1

print("Count of even numbers in number_list:",count)