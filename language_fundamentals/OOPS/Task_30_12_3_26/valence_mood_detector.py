class MoodDetector:

    def __init__(self,name,mood):
        self.track_name = name
        self.mood = mood

    def check_valence_mood(self):

        print("Track name:",self.track_name)

        if self.mood == "happy":
            print("Valence mood:happy")
        elif self.mood == "sad":
            print("Valence mood:sad")
        else:
            print("Valence mood:neutal")

mood_detector_inst = MoodDetector("Someone like you","sad")
mood_detector_inst.check_valence_mood()