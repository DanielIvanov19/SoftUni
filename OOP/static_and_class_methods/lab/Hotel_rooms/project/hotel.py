from typing import List

from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []


    @property
    def guests(self):
        return sum([r.guests for r in self.rooms])


    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f'{stars_count} stars Hotel')


    def add_room(self, room: Room):
        self.rooms.append(room)


    def take_room(self, room_number: int, people: int):

        room = [r for r in self.rooms if r.number == room_number][0]
        result = room.take_room(people)
        return result


    def free_room(self, room_number: int):
        room = [r for r in self.rooms if r.number == room_number][0]
        result = room.free_room()
        return result



    def status(self):
        free_rooms = [r for r in self.rooms if not r.is_taken]
        taken_rooms = [r for r in self.rooms if r.is_taken]
        return  f"Hotel {self.name} has {self.guests} total guests\n" \
                f"Free rooms: {', '.join([str(r.number)for r in free_rooms])}\n" \
                f"Taken: rooms: {', '.join([str(r.number)for r in taken_rooms])}"
