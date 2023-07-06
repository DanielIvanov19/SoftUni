class Music:
    def __init__(self, title: str, artist: str, lyrics: str):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self) -> str:
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self) -> str:
        return self.lyrics

    # def __str__(self) -> str:
        # return self.title
        # redefines the method print for the class object

m = Music("Godzilla", "Eminem", "...")
print(m.print_info())
print(m.lyrics)
print(m)