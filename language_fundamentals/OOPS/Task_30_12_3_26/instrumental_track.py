class InstrumentalTrack:
    def __init__(self,name,instrumentalness):
        self.track_name = name
        self.instrumentalness = instrumentalness

    def check_instrumentalness(self):

        print("Track name:",self.track_name)

        if self.instrumentalness == "vocal":
            print("Track contains only vocals")
        elif self.instrumentalness == "instrumental":
            print("Track contains only instruments.")
        else:
            print("Track contains both vocals and instruments.")

instrument_inst = InstrumentalTrack("Perfect","vocal")
instrument_inst.check_instrumentalness()