num = int(input("Enter number:"))

number = num

count = 0

while(number % 10 != 0):
    count = count + 1
    number = number // 10
print("Number of digits in",num,":",count)