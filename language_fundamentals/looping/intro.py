"""
execute block of statements particlular number of time

while
for

Syntax:= while loop

initialization
while(condition):
    stmt1
    stmt2
    incr/decr
"""

# w.a.p to display numbers from 1 to 10

i = 1           # i = 1
while(i <= 10): # 1 <= 10(T),2 <= 10(T),3 <= 10(T),4 <= 10(T),5 <= 10(T),6 <= 10(T),7 <= 10(T),8 <= 10(T),9 <= 10(T),10 <= 10(T),11 <= 10(F)
    print(i)    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    i = i+1     #2, 3, 4 , 5, 6, 7, 8, 9, 10, 11