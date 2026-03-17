num = int(input("Enter number:"))  #1234

while(num != 0):                   #1234 != 0(T)            #123 != 0(T)        #12 != 0        #1 != 0(T)  # 0 != 0(F)
    last_digit = num % 10          #1234 % 10 = 4           #123 % 10 = 3       #12 % 10 = 2    #1 % 10 = 1
    if last_digit % 2 == 0:        #4 % 2 == 0(T)           #3 % 2 == 0(F)      #2 % 2 == 0(T)  #1 % 2 == 0(F)
        print(last_digit)          #4                                           #2
    num = num // 10                #num = 123 = 1234 // 10  #12 = 123 // 10     #1 = 12 // 10   #0 = 1 // 10
