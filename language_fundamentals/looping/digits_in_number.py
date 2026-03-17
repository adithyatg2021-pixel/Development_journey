 
num = int(input("Enter number:"))

number = num

f = 1

count = len(str(num))

while(count != 0):
    f = num // (10 ** (count - 1))
    print(f)
    num = num % (10 ** (count - 1))
    count -= 1
