from csv import DictReader

class Spotify:
    def __init__(self):
        fr = open("language_fundamentals\\OOPS\\Task_30_12_3_26\\spotify-tracks-dataset.csv",encoding="utf-8")
        self.data = list(DictReader(fr))

    
class Genre(Spotify):
    def __init__(self):
        super().__init__()

    def show_genre(self):
        for di in self.data:
            track_name = di.get("track_name")
            print("Track name:",track_name)
            genre = di.get("track_genre")
            print("Track genre:",genre)

genre_inst = Genre()
genre_inst.show_genre()