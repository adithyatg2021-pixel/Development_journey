word1 = "silent"

word2 = "listen"

is_anagram = True

for ch in word1:
    if word2.find(ch) == -1:
            is_anagram = False
            break
if is_anagram == True:
      print("Anagram")
