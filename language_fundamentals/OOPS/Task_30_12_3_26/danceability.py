class DanceTrack:
    def __init__(self,track,danceability):
        self.name = track
        self.danceability = danceability

    def check_danceability(self):
        print("Track name:",self.name)
        if self.danceability > 0.70:
            print("Song is good for dance.")
        else:
            print("Not good for dancing.")

dance_track_inst = DanceTrack("Midnight groove",0.85)
dance_track_inst.check_danceability()