from csv import DictReader

class Spotify:
    def __init__(self):
        fr = open("language_fundamentals\\OOPS\\Task_30_12_3_26\\spotify-tracks-dataset.csv",encoding="utf-8")
        self.data = list(DictReader(fr))

class TrackSafety(Spotify):
    def __init__(self):
        super().__init__()

    def check_content(self):
        for di in self.data:
            print("Track name:",di.get("track_name"))
            print("Explicit or clean:",di.get("explicit"))

track_analyse_inst = TrackSafety() 
track_analyse_inst.check_content()