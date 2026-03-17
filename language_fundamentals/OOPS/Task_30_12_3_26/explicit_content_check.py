class TrackSafety:
    def __init__(self,name,explicit_clean):
        self.track_name = name
        self.explicit_clean = explicit_clean

    def check_content(self):
        print("Track name:",self.track_name)
        print("Explicit or clean:",self.explicit_clean)

track_analyse_inst = TrackSafety("In Da Club","Explicit") 
track_analyse_inst.check_content()