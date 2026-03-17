# break => exit from loop

for i in range(1,10): # i == 1      i == 2      i == 3      
    if i == 5:        # i == 5 (F)  2 == 5 (F)  3 == 5 (F)
        break         
    print(i)          # 1           2           3
print("End")