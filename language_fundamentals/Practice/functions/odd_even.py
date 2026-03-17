# odd = lambda n:"odd" if n % 2 != 0 else "even"
# print(odd(5))

# def amstrong(num):

#     count_dg = len(str(num))
#     number = num
#     sum_pow = 0

#     while(num != 0):
#         ld = num % 10
#         power = ld ** count_dg
#         sum_pow += power
#         num = num // 10

#     if sum_pow == number:
#         print("amstrong")

# amstrong(154)

# add_10 = lambda n : n+ 10
# print(add_10(5))

# mul_result = lambda n1,n2 : n1 * n2
# print(mul_result(2,3))

# lst = [1,2,3,4]

# square = list(map(lambda n : n **2 ,lst))
# print(square)

# even = list(filter(lambda n: n % 2 == 0,lst))
# print(even)

lst = ["hello","world","adithya","running","run","playing"]

len_5 = list(filter(lambda w: len(w) > 5,lst))
print(len_5)

