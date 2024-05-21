class Monster:
    """Base class for monsters."""

    def __init__(self, species, movement, attack, defend, hp, mp):
        self.movement = movement
        self.species = species
        self.attack = attack
        self.defend = defend
        self.hp = hp
        self.mp = mp

    def spawn(self):
        """Monster appears message."""
        spawn_message = f"{self.species} has appeared and advances to attack!"
        return spawn_message

    def creatue_attack(self):
        """Creature attack message."""
        attack_message = f"{self.species} is attacking!"

    def creatue_defend(self):
        """Creature defend message."""
        defend_message = f"{self.species} is defending!"

    def creature_description(self):
        """Creature description message."""
        long_desc = f"The {self.species} rolls {self.attack} dice to attack, and {self.defend} dice to defend. They can move up to {self.movement} spaces, have {self.hp}HP and {self.mp}MP"
        return long_desc


monster_01 = Monster("Zombie", 5, 2, 3, 1, 0)
monster_02 = Monster("Mummy", 4, 3, 4, 2, 0)
monster_03 = Monster("Gargoyle", 6, 4, 5, 3, 0)
monster_04 = Monster("Orc", 8, 3, 2, 1, 2)
monster_05 = Monster("Skeleton", 6, 2, 2, 1, 0)
monster_06 = Monster("Goblin", 10, 2, 1, 1, 1)
monster_07 = Monster("Chaos Warrior", 7, 4, 4, 3, 3)
monster_08 = Monster("Fimir", 6, 3, 3, 2, 3)
monster_09 = Monster("Chaos Warlock", 8, 3, 3, 1, 4)
