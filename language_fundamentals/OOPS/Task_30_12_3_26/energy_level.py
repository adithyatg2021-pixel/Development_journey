class EnergyLevel:
    def __init__(self,track_name,energy):
        self.track_name = track_name
        self.energy = energy

    def display(self):
        print("Track name:",self.track_name)
        if self.energy >= 75:
            print("High energy song")
        elif 50 <= self.energy < 75:
            print("Mediuam energy song")
        else:
            print("Low energy song")
        
energy_inst = EnergyLevel("Midnight pulse",78)
energy_inst.display()