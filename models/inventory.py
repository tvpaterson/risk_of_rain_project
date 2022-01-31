class Inventory:
    def __init__(self, character, item, id=None):
        self.character = character
        self.item = item
        self.items = []
        self.id = id
    