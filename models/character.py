class Character:

    def __init__(self, name, health, damage, armor, id = None):

        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
        self.items = []
        self.id = id
        