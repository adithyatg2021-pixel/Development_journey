word1 = "silent"

word2 = "listens"

con1 = True
con2 = True

if len(word1) == len(word2):
    for num in word1:
        if num not in word2 and word1.count(num) > 1:
            con1 = False
    for num in word2:
        if num not in word2 and word2.count(num) > 1:
            con2 = False

if con1 and con2 == True:
    print(word1,"and",word2,"is anagram.")
else:
    print(word1,"and",word2,"is not anagram.")
