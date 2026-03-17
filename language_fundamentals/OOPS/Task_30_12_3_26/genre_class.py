class Genre:

    def __init__(self,name,genre):
        self.track_name = name
        self.track_genre = genre

    def show_genre(self):
        print("Track name:",self.track_name)
        print("Track genre:",self.track_genre)

genre_inst = Genre("Midnight Echoes","Synthpop")
genre_inst.show_genre()