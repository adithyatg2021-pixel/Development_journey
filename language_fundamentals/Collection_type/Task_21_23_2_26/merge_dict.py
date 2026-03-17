
fruits_count1 = {"Apple":45,"Orange":90,"Mango":50,"Pineapple":80}

fruits_count2 = {"Mango":100,"Grapes":200,"Orange":150}

fruits_count3 = {}

for k,v in fruits_count1.items():
    fruits_count3[k] = v
for k,v in fruits_count2.items():
    for kk,vv in fruits_count3.items():
        if kk == k and v > vv:
            fruits_count3[k] = v
        elif kk == k and v < vv:
            fruits_count3[k] = vv
    fruits_count3[k] = v
print(fruits_count3)



