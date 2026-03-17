
def count_vowel(string):

    count = 0 
    VOWELS = "aeiou"
    for ch in string:
        if ch in VOWELS:
            count += 1
    return count

print("Number of vowels in \"arithmetic\" is",count_vowel("arithmetic"))