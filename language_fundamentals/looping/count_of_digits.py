num = int(input("Enter number:"))

count = 0

number = num

while(num != 0):
    count += 1
    num = num // 10
print("Number of digits in",number,":",count)
    