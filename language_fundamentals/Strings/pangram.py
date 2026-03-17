
string = "the quick brown fox jumps over lazy dog"

# string = "hello"

alphabets = "abcdefghijklmnopqrstuvwxyz"

is_pangram = True

# for ch in alphabets:
#     if ch not in string:
#         is_pangram = False
#         break
# if is_pangram == True:
#     print("Pangram")


for ch in alphabets:
    if string.find(ch) == -1:
        is_pangram = False
        break
print(is_pangram)