
dic = {"num1":23,"num2":13,"num3":89,"num4":56}
new_dic = dic.copy()

for k in dic.keys():
    if k == "num1" or k == "num2":
        new_dic.pop(k)
print(new_dic)