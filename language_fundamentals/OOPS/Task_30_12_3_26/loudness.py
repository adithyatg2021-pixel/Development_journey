class LoudnessCheck:
    def __init__(self,track_name,loudness):
        self.track_name = track_name
        self.loudness = loudness

    def classify_loud(self):
        print("Track name:",self.track_name)
        if self.loudness > 95:
            print("Loud")
        elif 80 < self.loudness <= 95:
            print("Medium")
        else:
            print("Soft")

loudness_init = LoudnessCheck("Dance party",10)
loudness_init.classify_loud()