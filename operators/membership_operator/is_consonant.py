
character = input("Enter the character:")

VOWELS = "AEIOUaeiou"

if character not in VOWELS:
    print("Consonant")
else:
    print("Vowel")