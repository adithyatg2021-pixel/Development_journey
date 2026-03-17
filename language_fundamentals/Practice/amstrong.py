num = int(input("Enter number:"))

sum = 0
number = num
length = len(str(num))

while num != 0:
    last_dg = num % 10
    sum += last_dg ** length
    num = num // 10

if sum == number:
    print(f"{number} is amstrong.")
else:
    print(f"{number} is not amstrong.")

