class PopularityCheck:

    def __init__(self,popularity):
        self.popularity = popularity

    def check_popularity(self):
        if self.popularity > 80:
            print("High popularity")
        elif 50 <= self.popularity < 80:
            print("Mediuam popularity")
        else:
            print("Low popularity")

track1 = PopularityCheck(70)
track1.check_popularity()