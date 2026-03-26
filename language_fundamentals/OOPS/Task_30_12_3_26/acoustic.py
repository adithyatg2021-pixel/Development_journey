from csv import DictReader
class Spotify:
    def __init__(self):
        fr = open("language_fundamentals\\OOPS\\Task_30_12_3_26\\spotify-tracks-dataset.csv",encoding="utf-8")
        self.data = list(DictReader(fr))
class AcousticTrack(Spotify):
    def __init__(self):
        super().__init__()

    def check_acoustic(self):
        for di in self.data:
            print("Track name:",di.get("track_name"))
            if float(di.get("acousticness")) > 0.5:
                print("Song is acoustic.")
            else:
                print("Non acoustic.")
acoustic_instance = AcousticTrack() 
acoustic_instance.check_acoustic()