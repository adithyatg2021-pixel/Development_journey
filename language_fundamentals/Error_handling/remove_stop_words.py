
def remove_stop_words(word):

    result = ""
    lst = word.split()
    try:
        fr = open("language_fundamentals\\Error_handling\\stop_words.txt")

        for line in fr:
            nline = line.rstrip("\n")
            if nline in lst:
                lst.remove(nline)
        for n in lst:
            result += n + " "
        result = result.strip()
        return result
        
    except Exception as e:
        print(e)


sentence = "machine learning is a subset of AI"

sentence1 = "django is a one of python framework"

assert remove_stop_words(sentence) == "machine learning subset AI","Test case 1 failed"
assert remove_stop_words(sentence1) == "django one python framework","Test case 2 failed"

print("Code accepted....")

