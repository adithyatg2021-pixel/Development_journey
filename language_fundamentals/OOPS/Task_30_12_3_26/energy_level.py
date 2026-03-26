from csv import DictReader

class Spotify:
    def __init__(self):
        fr = open("language_fundamentals\\OOPS\\Task_30_12_3_26\\spotify-tracks-dataset.csv",encoding="utf-8")
        self.data = list(DictReader(fr))

class EnergyLevel(Spotify):
    def __init__(self):
        super().__init__()
    
    def display(self):
        for di in self.data:
            print("Track name:",di.get("track_name"))
            if float(di.get("energy")) >= .75:
                print("High energy song")
            elif 50 <= float(di.get("energy")) < .75:
                print("Mediuam energy song")
            else:
                print("Low energy song")
        
energy_inst = EnergyLevel()
energy_inst.display()