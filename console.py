import pdb
from models.character import Character
from models.item import Item
import repositories.character_repository as character_repository
import repositories.item_repository as item_repository

# character_repository.delete_all()
# item_repository.delete_all()


character1 = Character('COMMANDO', 110, 12, 0)
character_repository.save(character1)

character2 = Character('ENGINEER', 110, 12, 0)
character_repository.save(character2)

character3 = Character('BANDIT', 110, 12, 0)
character_repository.save(character3)

character4 = Character('CAPTIAN', 110, 12, 0)
character_repository.save(character4)

character5 = Character('ACRID', 110, 12, 0)
character_repository.save(character5)

character6 = Character('ARTIFICER', 110, 12, 0)
character_repository.save(character6)

character7 = Character('HERETIC', 110, 12, 0)
character_repository.save(character7)

character8 = Character('HUNTRESS', 110, 12, 0)
character_repository.save(character8)

character9 = Character('LOADER', 110, 12, 0)
character_repository.save(character9)

character10 = Character('MERCENARY', 110, 12, 0)
character_repository.save(character10)

character11 = Character('MUL-T', 110, 12, 0)
character_repository.save(character11)

character12 = Character('REX', 110, 12, 0)
character_repository.save(character12)

item1 = Item('Sticky Bomb', 'DMG', 10, 'Chance to throw sticky bomb')
item_repository.save(item1)

item2 = Item('Topaz Brooch', 'ARM', 20, 'Gain temporary armor')
item_repository.save(item2)

item3 = Item('Medkit', 'HP', 20, 'Gain 20 health')
item_repository.save(item3)

item4 = Item('Bison Steak', 'HP', 25, 'Increase health by 25')
item_repository.save(item4)

item5 = Item('Ukulele', 'DMG', 100, 'Permanently increase damage by 100')
item_repository.save(item5)


# pdb.set_trace()