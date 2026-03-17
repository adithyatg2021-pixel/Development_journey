"""
E   O   E   O
O   E   O   E
E   O   E   O
O   E   O   E
"""

for r in range(1,5):
    for c in range(1,5):
        if (c+r) % 2 == 0:
            print("O",end="\t")
        else:
            print("E",end="\t")
    print()