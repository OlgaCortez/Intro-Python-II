# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    
    def move(self, direction):
        if self.current_room.cardinal_directions[direction] is not None:
            self.current_room = self.current_room.cardinal_directions[direction]
        else:
            print("You cannot move in this direction!")


    def __str__(self):
        return 'Name: {self.name}, Current Room: {self.current_room}'.format(self=self)