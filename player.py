class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room
        self.origin = ''

    def travel(self, direction, show_rooms=False):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            print(
                f"IM MOVING from {self.current_room.name} to {next_room.name}")
            self.current_room = next_room
            if (show_rooms):
                next_room.print_room_description(self)
        else:
            print("You cannot move in that direction.")
