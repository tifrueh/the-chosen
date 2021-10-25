from the_chosen.item import Item, Artifact, Artifacts


class Room:
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.links = {}
        self.vertical_links = {}
        self.hidden_links = {}
        self.characters = []
        self.items = []

    def describe(self):
        print(self.name)

        for n in range(0, len(self.name)-1):
            print("¯", end="")
        print("¯")

        print(self.description)

        for character in self.characters:
            character.describe()

        for item in self.items:
            if isinstance(item, Artifact) and item.get_initial_room() == self:
                item.describe_initial()
            else:
                item.describe()

        self.print_links()
        self.print_vertical_links()

    def print_links(self):
        if len(self.links) == 1:
            for direction in self.links:
                print(f"There is a door to the {direction}.")

        elif len(self.links) == 2:
            directions = []
            for direction in self.links:
                directions.append(direction)
            print(f"There are doors to the {directions[0]} and {directions[1]}.")

        elif len(self.links) == 3:
            directions = []
            for direction in self.links:
                directions.append(direction)
            print(f"There are doors to the {directions[0]}, {directions[1]} and {directions[2]}.")

        elif len(self.links) == 4:
            print("There are doors to all directions.")

    def print_vertical_links(self):
        if len(self.vertical_links) == 1:
            for direction in self.vertical_links:
                print(f"There is a ladder leading {direction}.")
        elif len(self.vertical_links) == 2:
            print("There is a ladder leading up and down.")

    def get_desc(self):
        return self.description

    def set_desc(self, new_description):
        self.description = new_description

    def get_name(self):
        return self.name

    def get_links(self):
        return self.links

    def link(self, direction, room):
        self.links[direction] = room

    def get_vertical_links(self):
        return self.vertical_links

    def link_vertical(self, direction, room):
        self.vertical_links[direction] = room

    def get_hidden_links(self):
        return self.hidden_links

    def link_hidden(self, direction, room):
        self.hidden_links[direction] = room

    def get_characters(self):
        return self.characters

    def get_character(self, name):
        for character in self.characters:
            if character.name.lower().replace(" ", "") == name.lower().replace(" ", ""):
                return character

    def add_character(self, character):
        self.characters.append(character)

    def remove_character(self, character):
        self.characters.remove(character)

    def get_items(self):
        return self.items

    def get_item(self, name):
        for item in self.items:
            if item.name.lower().replace(" ", "") == name.lower().replace(" ", ""):
                return item

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
