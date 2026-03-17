
num = [10, 45, 23, 89, 67, 89, 34]

num.sort()

for n in num:
    count_n = num.count(n)
    if count_n > 1:
        while count_n != 1:
            num.remove(n)
            count_n = count_n - 1

print("Second largest element:",num[len(num)-2])