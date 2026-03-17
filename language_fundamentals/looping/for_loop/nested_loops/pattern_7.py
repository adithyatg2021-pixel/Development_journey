for r in range(1,5):
    for c in range(1,5):
        if r == 1 or r == 3:
            print(1,end="\t")
        else:
            print(0,end="\t")
    print()