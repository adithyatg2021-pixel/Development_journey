
num = int(input("Enter number:"))  #6

i = 1
sum = 0

while(i <= num):    # 1 <= 6(T)         2 <= 6(T)       3 <= 6(T)
    sum += i        # sum = 1 = 0+1     sum = 3 = 1+2   sum = 6 = 3+3    
    i += 1          # 2                 3               4
print("Sum of first",num,"natural numbers:",sum)