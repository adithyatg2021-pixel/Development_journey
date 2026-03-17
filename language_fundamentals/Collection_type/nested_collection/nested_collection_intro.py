
"""
Colletion inside another collection

"""


social_media_posts = [
    [1,"Good morning",600,1200,"Arun"],
    [2,"Dance video",1000,4000,"Manu"],
    [3,"Music video",700,1200,"Vipin"],
    [4,"Food",3000,15000,"Keerthi"],
    [5,"Travel",5000,8000,"Priya"],
    [6,"Movies",12000,20000,"Hari"]
]


# insta views of keerthi

print("Insta views of keerthi",social_media_posts[3][3])   # 15000

# all facebook views

face_book_views = [lst[2] for lst in social_media_posts]
print("All face book views:",face_book_views)

insta_views = [lst[3] for lst in social_media_posts]
print("All insta views:",insta_views)

all_publishers = [lst[4] for lst in social_media_posts]
print("All publishers:",all_publishers)


# return the name of publishers whose post have face book views greater than 1000

face_book_post_filter = [lst[4] for lst in social_media_posts if lst[2] > 1000]
print("Name of publishers whose face book post have views greater than 1000:",face_book_post_filter)   
# ["Keerthi","Priya","Hari"]


# name of the publisher who have maximum insta views

max_insta_views = max([lst[3] for lst in social_media_posts])

max_insta_view_publisher = [lst[-1] for lst in social_media_posts if lst[3] == max_insta_views]

print("Name of the publisher who have maximum insta views:",max_insta_view_publisher)

# name of the publisher who have minimum FB views

min_fb_views = min([lst[2] for lst in social_media_posts])

min_fb_view_publisher = [lst[-1] for lst in social_media_posts if lst[2] == min_fb_views]

print("Name of the publisher who have minimum FB views:",min_fb_view_publisher)

