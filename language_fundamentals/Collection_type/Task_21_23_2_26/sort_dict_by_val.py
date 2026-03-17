
dic = {"num1":89,"num2":12,"num3":67,"num4":90,"num5":45}

sort_dic = {}
lis = []

for v in dic.values():
    lis.append(v)
    lis.sort()

for e in lis:
    for k in dic:
        if dic[k] == e:
            sort_dic[k] = e
print(sort_dic)

