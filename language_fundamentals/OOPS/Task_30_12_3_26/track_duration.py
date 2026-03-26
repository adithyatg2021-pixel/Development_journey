from csv import DictReader

class Spotify:

    def __init__(self):
        fr = open("language_fundamentals\\OOPS\\Task_30_12_3_26\\spotify-tracks-dataset.csv",encoding="utf-8")
        self.data = list(DictReader(fr))

class Track_dura(Spotify):
    def __init__(self):
        super().__init__()

    def millisec_minutes(self):
        for di in self.data:
            print(f"track_name:{di.get("track_name")},Duration in minutes:{int(di.get("duration_ms")) *  1.66666667 * (10 ** -5)}")

track_inst = Track_dura()
track_inst.millisec_minutes()