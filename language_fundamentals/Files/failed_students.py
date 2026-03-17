
fr1 = open("language_fundamentals\\Collection_type\\Files\\all_students.txt","r")

fr2 = open("language_fundamentals\\Collection_type\\Files\\passed_students.txt","r")

st1 = {line.rstrip("\n") for line in fr1}
st2 = {line.rstrip("\n") for line in fr2}

print("Failed students:",st1.difference(st2))

failed_stud = st1.difference(st2)

fw = open("language_fundamentals\\Collection_type\\Files\\failed_students.txt","w")

lst1 = [line.rstrip("\n") for line in fr1]
lst2 = [line.rstrip("\n") for line in fr2]

