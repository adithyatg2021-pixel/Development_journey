
# for r in range(1,5):
#     for c in range(1,5):
#         if c % 2 != 0:
#             print("O",end="\t")
#         else:
#             print("E",end="\t")
#     print()

# or

for r in range(1,5):
    for c in range(1,5):
        if c == 1 or c== 3:
            print("O",end="\t")
        else:
            print("E",end="\t")
    print()


