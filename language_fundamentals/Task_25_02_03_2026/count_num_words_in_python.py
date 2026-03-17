
fr = open("language_fundamentals\\Task_25_02_03_2026\\python.txt","r")
lst = []
count = 0

for line in fr:
    lst += line.split()
for w in lst:
    count += 1
print("Count of words in python.txt",count)