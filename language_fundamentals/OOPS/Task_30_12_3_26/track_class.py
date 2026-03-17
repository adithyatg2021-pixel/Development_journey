class Track:
    def __init__(self,track_name,artist,popularity):
        self.track_name = track_name
        self.artist = artist
        self.popularity = popularity

    def display_info(self):
        print("Track name:",self.track_name)
        print("Artist:",self.artist)
        print("Popularity:",self.popularity)

track_inst = Track("Die With A Smaile","Lady Gaga and Bruno Mars","1.7 billion")
track_inst.display_info()