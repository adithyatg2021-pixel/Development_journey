num = int(input("Enter number:"))

number = num

sum = 0

while(num != 0):
    last_digit = num % 10
    sum += last_digit ** 3
    num = num // 10
print("Sum of cube of digits in",number,":",sum)
