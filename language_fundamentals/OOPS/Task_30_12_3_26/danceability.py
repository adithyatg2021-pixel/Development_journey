from csv import DictReader

class Spotify:
    def __init__(self):
        fr = open("language_fundamentals\\OOPS\\Task_30_12_3_26\\spotify-tracks-dataset.csv",encoding="utf-8")
        self.data = list(DictReader(fr))

class DanceTrack(Spotify):
    def __init__(self):
        super().__init__()

    def check_danceability(self):
        for di in self.data:
            print("Track name:",di.get("track_name"))
            if float(di.get("danceability")) > .70:
                print("Song is good for dance.")
            else:
                print("Not good for dancing.")

dance_track_inst = DanceTrack("Midnight groove",0.85)
dance_track_inst.check_danceability()