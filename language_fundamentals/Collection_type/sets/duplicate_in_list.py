
numbers = [10,20,10,30,40,30,10,30,40,50,20]

# st = set()

# for num in numbers:
#     if numbers.count(num) > 1:
#         st.add(num)

# print(st)

st = {num for num in numbers if numbers.count(num) > 1}

print(st)