class TempoAnalyzer:
    def __init__(self,name,tempo):
        self.track_name = name
        self.tempo = tempo

    def analyze_tempo(self):
        print("Track name:",self.track_name)
        if self.tempo > 120:
            print("Fast")
        elif 76 < self.tempo <= 120:
            print("Medium")
        else:
            print("Slow")

temp_analyzer = TempoAnalyzer("Wipe out the DJ",180)
temp_analyzer.analyze_tempo()