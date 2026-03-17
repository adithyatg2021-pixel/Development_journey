class TrackSummary:
    def __init__(self,name,artist,genre,popularity):
        self.track_name = name
        self.artist = artist
        self.genre = genre
        self.popularity = popularity
    
    def summary(self):
        print("Track name:",self.track_name)
        print("Artist:",self.artist)
        print("Genre:",self.genre)
        print("Popularity:",self.popularity)

track_summary_inst = TrackSummary("Believer","Imagine Dragons","Rock",90)
track_summary_inst.summary()