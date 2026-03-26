from csv import DictReader
class Spotify:
    def __init__(self):
        fr = open("language_fundamentals\\OOPS\\Task_30_12_3_26\\spotify-tracks-dataset.csv",encoding="utf-8")
        self.data = list(DictReader(fr))
class LoudnessCheck(Spotify):
    def __init__(self):
        super().__init__()
    
    def classify_loud(self):
        for di in self.data:
            print("Track name:",di.get("track_name"))
            if float(di.get("loudness")) > -2.5:
                print("Loud")
            elif -5.0 < float(di.get("loudness")) <= -2.5:
                print("Medium")
            else:
                print("Soft")
loudness_init = LoudnessCheck()
loudness_init.classify_loud()