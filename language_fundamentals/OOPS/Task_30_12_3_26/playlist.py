from csv import DictReader

class PlayList: 
    def add_track(self):
        fr = open("language_fundamentals\\OOPS\\Task_30_12_3_26\\spotify-tracks-dataset.csv",encoding="utf-8")
        self.data = list(DictReader(fr))
        self.tracks = [di.get("track_name") for di in self.data]

    def display(self):
        print(self.tracks)

    def count(self):
        count = 0
        for i in self.tracks:
            count += 1
        print("Count of tracks:",count)

track_inst = PlayList()
track_inst.add_track()
track_inst.display()
track_inst.count()
