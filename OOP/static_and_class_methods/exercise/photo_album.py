from math import ceil


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for i in range(pages)]
        self.current_row_index = 0
    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label: set):

        if len(self.photos[self.current_row_index]) == 4:
            self.current_row_index += 1
        try:
            self.photos[self.current_row_index].append(label)
            return f"{label} photo added successfully on page {self.current_row_index+1} slot {len(self.photos[self.current_row_index])}"
        except IndexError:
            return "No more free slots"

    def display(self):
        res = "-" * 11 + "\n"
        for page in self.photos:
            res += " ".join(["[]"for photo_name in page]) + "\n"
            res += "-" * 11 + "\n"
        return res



album = PhotoAlbum(2)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.display())



