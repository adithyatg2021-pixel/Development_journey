# continue => skip current iteration

for i in range(1,10):
    if i == 5:
        continue
    print(i)
print("End")
"""
expected output:
1
2
3
4
6
7
8
9
End
"""