"""
syntax: sequence[start:stop]
"""


text = "python programming"

print(text[0:6]) # 0 to 5 -> python
print(text[7:18]) # 7 to 17 ->programming
print(text[:6]) # default value 0 for start -> python
print(text[7:]) # default value lenth of the string -> programming