from csv import DictReader

class Spotify:

    def __init__(self):
        fr = open("language_fundamentals\\OOPS\\Task_30_12_3_26\\spotify-tracks-dataset.csv",encoding="utf-8")
        self.data = list(DictReader(fr))

class PopularityCheck(Spotify):
    def __init__(self):
        super().__init__()
        
    def check_popularity(self):
        for di in self.data:
            if int(di.get("popularity")) > 80:
                print(f"Track name:{di.get("track_name")},popularity: High")
            elif 50 <= int(di.get("popularity")) <= 80:
                print(f"Track name:{di.get("track_name")},popularity: Medium")
            else:
                print(f"Track name:{di.get("track_name")},popularity: Low")


track = PopularityCheck()
track.check_popularity()