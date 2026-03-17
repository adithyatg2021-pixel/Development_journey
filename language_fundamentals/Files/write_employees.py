
employees = ["hari","karthik","reena","niya","manu"]

fw = open("language_fundamentals\\Collection_type\\Files\\employees.txt","w")

for e in employees:
    fw.write(e+"\n")

print("Completed....")