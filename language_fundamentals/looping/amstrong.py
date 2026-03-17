num = int(input("Enter number:"))   #153

number = num                        #number = 153

result = 0                          #result = 0

number_length = len(str(num))       #number_length = 3 = len("123") = len(str(num))

while(num != 0):                    #153 != 0(T)
    digit = num % 10                #3 = 153 % 10
    expo = digit ** number_length   #expo = 27 = 3 ** 3
    result += expo                  #result = 0 + 27
    num = num // 10                 #num = 15 = 153 // 10
if number == result:                
    print(number,"is amtrong")
else:
    print(number,"is not amstrong")