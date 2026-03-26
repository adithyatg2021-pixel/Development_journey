from csv import DictReader

class Spotify:

    def __init__(self):
        fr = open("language_fundamentals\\OOPS\\Task_30_12_3_26\\spotify-tracks-dataset.csv",encoding="utf-8")
        self.data = list(DictReader(fr))

class Track(Spotify):

    def __init__(self):
        super().__init__()

    def display_info(self):

        for di in self.data:
            print(f"Track name:{di.get("track_name")},Artist:{di.get("artists")},Popularity:{di.get("popularity")}")

track_inst = Track()
track_inst.display_info()







        