class AcousticTrack:
    def __init__(self,name,acousticness):
        self.track_name = name
        self.acousticness = acousticness

    def check_acoustic(self):
        print("Track name:",self.track_name)
        if 0.0 <= self.acousticness <= 1.0:
            print("Song is acoustic.")
            print("Acoustic value:",self.acousticness)
        else:
            print("Non acoustic.")

acoustic_instance = AcousticTrack("Perfect",0.65) 
acoustic_instance.check_acoustic()