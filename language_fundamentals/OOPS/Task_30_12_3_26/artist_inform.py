from csv import DictReader

class Spotify:
    def __init__(self):
        fr = open("language_fundamentals\\OOPS\\Task_30_12_3_26\\spotify-tracks-dataset.csv",encoding="utf-8")
        self.data = list(DictReader(fr))

class Artist(Spotify):
    def __init__(self):
        super().__init__()

    def display(self):
        for di in self.data:
            print("Name of artist:",di.get("artists"),",Track genre:",di.get("track_genre"),",Popularity:",di.get("popuarity"))
    
artist_inst = Artist()
artist_inst.display()