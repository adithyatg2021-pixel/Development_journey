
fa = open("language_fundamentals\\Task_25_02_03_2026\\python.txt","a")

fr = open("language_fundamentals\Task_25_02_03_2026\python1.txt","r")

for line in fr:
    fa.write(line)

print("Completed....")