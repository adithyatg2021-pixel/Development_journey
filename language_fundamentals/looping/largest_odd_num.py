num = int(input("Enter number:"))

while(num != 0):
    last_digit = num % 10
    if last_digit % 2 != 0:
        print(num)
        break
    else:
        num = num // 10
        