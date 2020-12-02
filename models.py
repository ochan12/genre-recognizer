class Features:
    def __init__(self, genre, tempo=None, beat=None, tempogram=None) -> None:
        self.tempo = tempo
        self.beat = beat
        self.tempogram = tempogram
        self.genre = genre

    def to_dict(self):
        return dict({
            "tempo": self.tempo, 
            "beat": self.beat, 
            "tempogram": self.tempogram, 
            "genre": self.genre
        })