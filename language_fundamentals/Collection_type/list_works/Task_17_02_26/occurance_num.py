
num = int(input("Enter the number to check it's frequency:"))

count = 0

num_list = [23,45,89,23,12,80,12,89,45]

for number in num_list:
    if number == num:
        count += 1

print(f"Frequency of {num} in the list: {count}")

