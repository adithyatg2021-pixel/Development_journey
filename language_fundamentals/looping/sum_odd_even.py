"""
w.a.p to display sum of odd numbers and sum of even numbers upto limit
"""

limit = int(input("Enter limit:"))          #6

i = 1                                       # i = 1

sum_of_even = 0                             # sum_of_even = 0
sum_of_odd = 0                              # sum_of_odd = 0

while(i <= limit):                          # 1 <= 6(T)
    if i % 2 == 0:                          # 1 % 2 == 0(F)
        sum_of_even += i
    else:
        sum_of_odd += i                     #sum_of_odd = 1 = 0+1
    i += 1                                  #2

print("Sum of even numbers upto",limit,":",sum_of_even)
print("Sum of odd numbers upto",limit,":",sum_of_odd)
