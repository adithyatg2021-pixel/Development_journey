num = int(input("Enter number:"))

count = 0
number  = num
while num != 0:
    ls_gt = num % 10
    count += 1
    num = num // 10

print(count)
