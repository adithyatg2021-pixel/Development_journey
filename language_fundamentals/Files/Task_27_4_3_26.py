from csv import DictReader
from csv import DictWriter
fr = open("language_fundamentals\\Collection_type\\Files\\movie.csv")

data = list(DictReader(fr))

# for i in range(0,5):
    # print(data[i])

# Count of movie records

count_of_movie_records = len([m for m in data])
# print("Number of movie records:",count_of_movie_records)

# All headers from movie.csv

# for da in data:
#     print(da.keys())
#     break

# Year and movies

# year = int(input("Enter year:"))

# movie_titles_in_year = [da.get("Name") for da in data if int(da.get("Year_of_Release")) == year]
# print("Movies in",year,":",movie_titles_in_year)

# movie with heighest rating

heighest_rating = max([da.get("Rating") for da in data])

heighest_rating_movie = [da.get("Name") for da in data if da.get("Rating") == heighest_rating]

# print("Heighest rating movie:",heighest_rating_movie)

# Genre

# genre = input("Genre:")

# genre_movies = [da.get("Name") for da in data if da.get("Movie_Categories") == genre]

# print(f"{genre} movies:{genre_movies}")

# top rated movies to top_rated.csv

# fw = open("language_fundamentals\\Collection_type\\Files\\top_rated_movies.csv","w")

# #     #top_rated = [da for da in data if float(da.get("Rating"))>8.0]

# lst_rate= [da for da in data if float(da.get("Rating"))>8.0]
# for j in range(0,len(lst_rate)):
#     l = str(lst_rate[j]).strip("{")
#     r = l.strip("}")
#     fw.write(r)
#     fw.write("\n")
#         #DictReader(fw)


# genre_count

# genre_count = {}

# for da in data:
#     genre = da.get("Movie_Categories")
#     genre_c = 1
#     if genre in genre_count:
#         genre_count[genre] += genre_c + 1
#     else:
#         genre_count[genre] = genre_c

# fgw = open("language_fundamentals\\Collection_type\\Files\\genre_count.txt","w")

# for k,v in genre_count.items():
#     fgw.write(f"{k}:{v}")
#     fgw.write("\n")

# all_movies sorted in descending order of rating

sorted_rating = sorted(data,key=lambda da:da.get("Rating"),reverse=True)

fw = open("language_fundamentals\\Collection_type\\Files\\sorted_movies.csv","w")
# for da in sorted_rating:
#     fw.write(str(da))
#     fw.write("\n")



