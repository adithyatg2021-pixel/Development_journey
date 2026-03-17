def extract_skills(title):

    lst = []

    fr = open("language_fundamentals\\Error_handling\\skills_dataset.txt")

    for line in fr:
        l = line.lstrip("### ")
        r = l.rstrip("\n")
        lst.append(r)
    print(lst)
    for i in range(0,len(lst)):
        if lst[i] == title.upper():
            while(lst[i] != ''):
                print(lst[i])
                i = i+1
   
extract_skills("data & analytics")