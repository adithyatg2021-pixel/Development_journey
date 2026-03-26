from csv import DictReader
class Spotify:
    def __init__(self):
        fr = open("language_fundamentals\\OOPS\\Task_30_12_3_26\\spotify-tracks-dataset.csv",encoding="utf-8")
        self.data = list(DictReader(fr))
class TempoAnalyzer(Spotify):
    def __init__(self):
        super().__init__()

    def analyze_tempo(self):
        for di in self.data:
            print("Track name:",di.get("track_name"))
            if float(di.get("tempo")) > 120.0:
                print("Fast")
            elif 76 < float(di.get("tempo")) <= 120.0:
                print("Medium")
            else:
                print("Slow")
temp_analyzer = TempoAnalyzer()
temp_analyzer.analyze_tempo()