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

    def creature_defend(self):
        """Creature defend message."""
        defend_message = f"{self.species} is defending!"

    def creature_description(self):
        """Creature description message."""
        long_desc = f"The {self.species} rolls {self.attack} dice to attack, and {self.defend} dice to defend. They can move up to {self.movement} spaces, have {self.hp}HP and {self.mp}MP"
        return long_desc


creatures = {
    "monster01": {
        "species": "Zombie",
        "movement": 5,
        "attack": 2,
        "defend": 3,
        "hp": 1,
        "mp": 1,
    },
    "monster02": {
        "species": "Gargoyle",
        "movement": 6,
        "attack": 4,
        "defend": 5,
        "hp": 3,
        "mp": 0,
    },
    "monster03": {
        "species": "Gargoyle",
        "movement": 6,
        "attack": 4,
        "defend": 5,
        "hp": 3,
        "mp": 0,
    },
    "monster04": {
        "species": "Orc",
        "movement": 8,
        "attack": 3,
        "defend": 2,
        "hp": 1,
        "mp": 2,
    },
    "monster05": {
        "species": "Skeleton",
        "movement": 6,
        "attack": 2,
        "defend": 2,
        "hp": 1,
        "mp": 0,
    },
    "monster06": {
        "species": "Goblin",
        "movement": 10,
        "attack": 2,
        "defend": 1,
        "hp": 1,
        "mp": 1,
    },
    "monster07": {
        "species": "Chaos Warrior",
        "movement": 7,
        "attack": 4,
        "defend": 4,
        "hp": 3,
        "mp": 3,
    },
    "monster08": {
        "species": "Fimir",
        "movement": 6,
        "attack": 3,
        "defend": 3,
        "hp": 2,
        "mp": 3,
    },
    "monster09": {
        "species": "Chaos Warlock",
        "movement": 8,
        "attack": 3,
        "defend": 3,
        "hp": 1,
    },
}

print(creatures["monster06"])
