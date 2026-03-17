
movies = [
    [1, "K.G.F: Chapter 1", "Yash", "Kannada", 8.2, 1234567],
    [2, "K.G.F: Chapter 2", "Yash", "Kannada", 8.3, 678900],
    [3, "K.G.F: Chapter 3", "Yash", "Kannada", 9.5, 456789], 
    [4, "Salaar: Part 1 – Ceasefire", "Prabhas", "Telugu", 6.5, 45678567],
    [5, "Pushpa 2: The Rule", "Allu Arjun", "Telugu", 10.0, 1234567], 
    [6, "Aavesham", "Fahadh Faasil", "Malayalam", 7.9, 1234567]
]

# display all movie title

all_movie_title = [lst[1] for lst in movies]
# print(all_movie_title)

# movie with top rating

top_rating = max([lst[4] for lst in movies])
movie_name_with_top_rating = [lst[1] for lst in movies if lst[4] == top_rating]
# print(movie_name_with_top_rating)

# display kannada movies

movies_in_kannada_lan = [lst[1] for lst in movies if lst[3] == "Kannada"]
# print(movies_in_kannada_lan)

# display movies whre actor is yash

movies_of_yash = [lst[1] for lst in movies if lst[2] == "Yash"]
# print(movies_of_yash)

# which language most number of movies

languages = [lst[3] for lst in movies]
language_count = {lan:languages.count(lan) for lan in languages}
# maximum = 0
# for k,v in language_count.items():
#     if v > maximum:
#         maximum = v
#         key = k
# print(key)

language_count_list = [[v,k] for k,v in language_count.items()]
sorted_language_count_list = sorted(language_count_list,reverse=True)
print("Language with most movies:",sorted_language_count_list[0][1])

# movie with max budget

max_budget = max([lst[5] for lst in movies])
max_budget_movie = [lst[1] for lst in movies if lst[-1] == max_budget]
# print("Maximum budget movie:",max_budget_movie)

# languages

languages = {lst[3] for lst in movies}
# print("Movie languages:",languages)