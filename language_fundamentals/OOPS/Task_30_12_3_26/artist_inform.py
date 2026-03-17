class Artist:
    def __init__(self,name,track):
        self.artist_name = name
        self.track_name = track

    def display(self):
        print("Name of artist:",self.artist_name)
        print("Track name:",self.track_name)

artist_inst = Artist("Aarav Menon","Midnight Echoes")
artist_inst.display()