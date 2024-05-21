class Player:
    """Base class for player characters."""

    def __init__(self, char_class, attack, defend, hp, mp, movement, weapon):
        self.char_class = char_class
        self.attack = attack
        self.defend = defend
        self.hp = hp
        self.mp = mp
        self.movement = movement
        self.weapon = weapon

    def player_attack(self):
        """Player attack message."""
        attack_message = f"{self.char_class} is attacking rolling {self.attack} dice!"
        return attack_message

    def player_defend(self):
        """Player defence message."""
        defend_message = f"{self.char_class} is defending rolling {self.defend} dice!"
        return defend_message


player_01 = Player("Barbarian", 3, 2, 8, 2, 2, "broadsword")
player_02 = Player("Dwarf", 2, 2, 7, 3, 2, "shortsword")
player_04 = Player("Elf", 2, 2, 6, 4, 2, "shortsword")
player_04 = Player("Wizard", 1, 2, 4, 6, 2, "dagger")
