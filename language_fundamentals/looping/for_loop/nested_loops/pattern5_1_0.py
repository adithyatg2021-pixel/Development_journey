for r in range(1,4):
    for c in range(1,4):
        if r == c:
            print(1,end="\t")
        else:
            print(0,end="\t")
    print()