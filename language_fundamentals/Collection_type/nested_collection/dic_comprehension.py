
lst = [10,11,12,11,10,13,13]

#expected output num:freq

num_count = {n:lst.count(n) for n in lst}
print(num_count)