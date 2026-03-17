
num =  [10, 20, 30, 20, 40, 10, 50]

for n in num:
    count_n = num.count(n)
    if count_n > 1:
        while count_n != 1:
            num.remove(n)
            count_n = count_n - 1
print(num)
