"""
w.a.p to print first vowel in a word
"""

word = input("Enter word:")

VOWELS = "aeiou"

for ch in word:
    if ch in VOWELS:
        print(ch)
        break
    