
languages=["thamil","malayalam","kannada","telungu","kannada","telungu","thamil","malayalam","thamil","malayalam"]

language_count = {lan:languages.count(lan) for lan in languages}

print(language_count)

language_count_lst = [[v,k] for k,v in language_count.items()]

print("Sorted languages with count:",sorted(language_count_lst,reverse=True))