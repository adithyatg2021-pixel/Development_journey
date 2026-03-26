from csv import DictReader
class Spotify:
    def __init__(self):
        fr = open("language_fundamentals\\OOPS\\Task_30_12_3_26\\spotify-tracks-dataset.csv",encoding="utf-8")
        self.data = list(DictReader(fr))
class InstrumentalTrack(Spotify):
    def __init__(self):
        super().__init__()
    def check_instrumentalness(self):
        for di in self.data:
            print("Track name:",di.get("track_name"))

            if float(di.get("instrumentalness")) > 7.0:
                print("Track contains only vocals")
            elif float(di.get("instrumentalness")) <= 7.0:
                print("Track contains only instruments.")
            else:
                print("Track contains both vocals and instruments.")
instrument_inst = InstrumentalTrack()
instrument_inst.check_instrumentalness()