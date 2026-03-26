from csv import DictReader
class Spotify:
    def __init__(self):
        fr = open("language_fundamentals\\OOPS\\Task_30_12_3_26\\spotify-tracks-dataset.csv",encoding="utf-8")
        self.data = list(DictReader(fr))
class MoodDetector(Spotify):
    def __init__(self):
        super().__init__()
    def check_valence_mood(self):
        for di in self.data:
            print("Track name:",di.get("track_name"))
            if float(di.get("valence")) > 0.7:
                print("Valence mood:happy")
            elif 0.5 < float(di.get("valence")) <= 0.7:
                print("Valence mood:sad")
            else:
                print("Valence mood:neutal")
mood_detector_inst = MoodDetector()
mood_detector_inst.check_valence_mood()