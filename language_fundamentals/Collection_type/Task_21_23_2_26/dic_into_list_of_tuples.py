
fruits_count = {"Apple":45,"Orange":90,"Mango":50,"Pineapple":80}
lis = []
tup = tuple()

for k,v in fruits_count.items():
    tup = k,v
    lis.append(tup)
print(lis)
