# The Chosen  Copyright (C) 2021  Timo Früh
# Full copyright notice in main.py

class Player:
    def __init__(self, player_name, starting_room):
        self.name = player_name
        self.inventory = []
        self.current_room = starting_room
        self.kills = 0

    def move(self, direction):
        if direction in self.current_room.get_links():
            self.current_room = self.current_room.get_links()[direction]
        elif direction in self.current_room.get_vertical_links():
            print(f"You climb {direction} the ladder.\n")
            self.current_room = self.current_room.get_vertical_links()[direction]
        elif direction in self.current_room.get_hidden_links():
            print(f"As you lay your hand upon the {direction} wall, you pass through it and emerge on the other side.\n")
            self.current_room = self.current_room.get_hidden_links()[direction]
        else:
            print("You can't go that way.")
            print("")

    def get_inventory(self):
        return self.inventory

    def get_inventory_item(self, name):
        for item in self.inventory:
            if item.get_name().lower().replace(" ", "") == name.lower().replace(" ", ""):
                return item

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def remove_from_inventory(self, item):
        self.inventory.remove(item)

    def get_name(self):
        return self.name

    def get_current_room(self):
        return self.current_room

    def get_kills(self):
        return self.kills

    def add_kill(self):
        self.kills += 1
