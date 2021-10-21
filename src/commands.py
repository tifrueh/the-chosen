from character import Character, Enemy, Friend


class Commands:
    
    commands = {"north     ": "  move north",
                "east      ": "  move east",
                "south     ": "  move south",
                "west      ": "  move west",
                "look      ": "  look at your surroundings",
                "talk      ": "  talk to someone in the room",
                "inventory ": "  show what you are carrying",
                "fight     ": "  fight someone",
                "take      ": "  put something into your inventory",
                "drop      ": "  drop something in your inventory",
                "hug       ": "  hug someone",
                "quit      ": "  quit the game -> NOTE: you will not be able to restore the game later",
                "help      ": "  show this list"}
    
    @classmethod
    def print_commands(cls):
        for command in cls.commands:
            print(f"{command}:{cls.commands[command]}")

    @staticmethod
    def movement(player, direction):
        player.move(direction)
        player.get_current_room().describe()

    @staticmethod
    def look(player):
        player.get_current_room().describe()

    @staticmethod
    def talk(player):
        if player.get_current_room().get_characters():
            user_input = input("Talk to whom? ")
            talk_to = user_input.lower().replace(" ", "")
            character = player.get_current_room().get_character(talk_to)

            if character:
                character.talk()

            else:
                print(f"There is no {user_input} here.")

        else:
            print("There is no one here to listen to your beautiful voice.")

    @staticmethod
    def show_inventory(player):
        if player.get_inventory():
            print("You are carrying:")
            for item in player.get_inventory():
                print(f"- {item.get_name_w_cap_art()}")
        else:
            print("You are empty-handed.")

    @staticmethod
    def fight(player):
        alive = True

        if player.get_current_room().get_characters():
            user_input = input("Fight whom? ")
            fight = user_input.lower().replace(" ", "")
            enemy = player.get_current_room().get_character(fight)

            if enemy:
                fight_with = input("What do you want to fight with? ").lower().replace(" ", "")
                weapon = player.get_inventory_item(fight_with)

                if weapon:
                    alive = player.get_current_room().get_character(fight).fight(weapon, player)
                else:
                    print(f"You do not have a {fight_with}.")

            else:
                print(f"There is no {user_input} here.")

        else:
            print("There is no one here to fight.")

        return alive

    @staticmethod
    def take(player):
        if player.get_current_room().get_items():
            user_input = input("What do you want to take? ")
            take = user_input.lower().replace(" ", "")
            item = player.get_current_room().get_item(take)

            if item:
                player.get_current_room().remove_item(item)
                player.add_to_inventory(item)
                print("Taken.")
            else:
                print(f"There is no {user_input} here.")

        else:
            print("There is nothing here to take.")

    @staticmethod
    def drop(player):
        if player.get_inventory():
            user_input = input("What do you want do drop? ")
            drop = user_input.lower().replace(" ", "")
            item = player.get_inventory_item(drop)

            if item:
                player.remove_from_inventory(item)
                player.get_current_room().add_item(item)
                print("Dropped.")
            else:
                print(f"You do not have a {user_input}.")

        else:
            print("You do not have anything to drop.")

    @staticmethod
    def hug(player):
        if player.get_current_room().get_characters():
            user_input = input("Hug whom? ")
            hug = user_input.lower().replace(" ", "")
            character = player.get_current_room().get_character(hug)

            if character:
                if isinstance(character, Friend):
                    character.hug()
                elif isinstance(character, Enemy):
                    print("You wouldn't want to hug this malicious creature.")
                elif isinstance(character, Character):
                    print("I doubt they'd appreciate that.")

            else:
                print(f"There is no {user_input} here.")

        else:
            print("There is no one here to receive your comforting embrace.")

    @staticmethod
    def quit():
        confirm = input("Do you really whish to leave the game? (y is affermative) ")
        return confirm
