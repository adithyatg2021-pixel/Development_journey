
num = int(input("Enter number:"))    # 6

i = 1                                # i = 1
sum = 0                              # sum  = 0

while(i <= num):                     # 1 <= 6(T)
    if i % 2 == 0:                   # 1 % 2 == 0(f)
        sum += i
    i += 1                           # 2
print("Sum of even numbers upto",num,":",sum)