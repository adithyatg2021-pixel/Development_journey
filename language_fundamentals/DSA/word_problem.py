source = "traviduxtechnology"

target = "vridautx"
present = True
for ch in target:
    if ch not in source:
        present = False
        break

print(present)
