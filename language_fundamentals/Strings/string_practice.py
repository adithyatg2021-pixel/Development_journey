
# text = "ihave2pen1pencilandonecar"

# # w.a.p to display digits in this text

# for ch in text:
#     if ch.isdigit():
#         print(ch)

word = "aman##aplan**panamawith2car1bike"

# w.a.p to display alphabet_count,digiit_count,special_char_count

alphabet_count = 0
digit_count = 0
special_char_count = 0

for ch in word:
    if ch.isalpha():
        alphabet_count += 1
    elif ch.isdigit():
        digit_count += 1
    elif not ch.isalnum():
        special_char_count += 1

print("Count of alphabets:",alphabet_count)
print("Count of digits:",digit_count)
print("Count of special characters:",special_char_count)

