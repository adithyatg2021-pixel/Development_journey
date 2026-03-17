num = int(input("Enter number:"))   #234

while(num != 0):                    # 234 != 0(T)                   # 23 != 0(T)    # 2 != 0(T)     # 0 != 0(F)
    last_digit = num % 10           # last_digit = 4 = 234 % 10     # 3 = 23 % 10   # 2 % 10 = 2
    print(last_digit)               # 4                             # 3             # 2
    num = num // 10                 # num = 23 = 234 // 10          # 2 = 23 // 10  # 0 = 2 // 10
