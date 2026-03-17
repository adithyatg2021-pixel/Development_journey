num = int(input("Enter number:"))

count = 0

number = num

reverse = ""

while(number % 10 != 0):
    rn = number % 10
    reverse += str(rn)
    number = number // 10
print("Reverse of the number:",reverse)


