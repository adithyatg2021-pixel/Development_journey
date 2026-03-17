class Track:
    def __init__(self,track_name,duration):
        self.track_name = track_name
        self.duration = duration

    def millisec_minutes(self):
        print("Track name:",self.track_name)
        print("Duration in minutes:",self.duration * 1.66666667 * (10 ** -5))

track_inst = Track("Bohemian Rhapsody",355000)
track_inst.millisec_minutes()