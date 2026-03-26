from csv import DictReader
class Spotify:
    def __init__(self):
        fr = open("language_fundamentals\\OOPS\\Task_30_12_3_26\\spotify-tracks-dataset.csv",encoding="utf-8")
        self.data = list(DictReader(fr))
class TrackSummary(Spotify):
    def __init__(self):
        super().__init__()

    def summary(self):
        for di in self.data:
            print(f"Track name:{di.get("track_name")}, Artist:{di.get("artists")}, Genre:{di.get("track_genre")}, Popularity:{di.get("popularity")}")
track_summary_inst = TrackSummary()
track_summary_inst.summary()