"""
w.a.p to create two lists for positive and negative numbers from given list
"""


numbers = [-45,90,78,-2,-12,67]

positive_list = []
negative_list = []

for num in numbers:
    if num > 0:
        positive_list.append(num)
    elif num < 0:
        negative_list.append(num)

print("List of positive numbers",positive_list)
print("List of negative numbers",negative_list)
