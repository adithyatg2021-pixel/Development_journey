def count_spam_words(message):
    count = 0
    lst = message.split()

    fr = open("language_fundamentals\\Error_handling\\spam_words.txt")

    for line in fr:
        nline = line.rstrip("\n")

        if nline in lst:
            count += 1

    return count

print(count_spam_words("you win free cash"))