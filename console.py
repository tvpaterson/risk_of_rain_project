import pdb
from models.character import Character
from models.item import Item

import repositories.character_repository as character_repository
import repositories.item_repository as  item_repository



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

character7 = Character('HUNTRESS', 110, 12, 0)
character_repository.save(character7)

character8 = Character('LOADER', 110, 12, 0)
character_repository.save(character8)

character9 = Character('MERCENARY', 110, 12, 0)
character_repository.save(character9)

character10 = Character('MUL-T', 110, 12, 0)
character_repository.save(character10)

character11 = Character('REX', 110, 12, 0)
character_repository.save(character11)


item1 = Item('Sticky Bomb', 'DMG', 10, 'Chance to throw sticky bomb', character1)
item_repository.save(item1)

item2 = Item('Topaz Brooch', 'ARM', 20, 'Gain temporary armor', character1)
item_repository.save(item2)

item3 = Item('Medkit', 'HP', 20, 'Gain 20 health', character1)
item_repository.save(item3)

item4 = Item('Bison Steak', 'HP', 25, 'Increase health by 25', character1)
item_repository.save(item4)

item5 = Item('Ukulele', 'DMG', 100, 'Permanently increase damage by 100', character1)
item_repository.save(item5)

item6= Item('Sticky Bomb', 'DMG', 10, 'Chance to throw sticky bomb', character2)
item_repository.save(item6)

item7 = Item('Topaz Brooch', 'ARM', 20, 'Gain temporary armor', character2)
item_repository.save(item7)

item8 = Item('Topaz Brooch', 'ARM', 20, 'Gain temporary armor', character3)
item_repository.save(item8)

item9 = Item('Medkit', 'HP', 20, 'Gain 20 health', character3)
item_repository.save(item9)

item10 = Item('Bison Steak', 'HP', 25, 'Increase health by 25', character4)
item_repository.save(item10)

item11 = Item('Ukulele', 'DMG', 100, 'Permanently increase damage by 100', character4)
item_repository.save(item11)

item12 = Item('Medkit', 'HP', 20, 'Gain 20 health', character5)
item_repository.save(item12)

item13 = Item('Ukulele', 'DMG', 100, 'Permanently increase damage by 100', character5)
item_repository.save(item13)

item14 = Item('Topaz Brooch', 'ARM', 20, 'Gain temporary armor', character6)
item_repository.save(item14)

item15 = Item('Sticky Bomb', 'DMG', 10, 'Chance to throw sticky bomb', character7)
item_repository.save(item15)

item16 = Item('Medkit', 'HP', 20, 'Gain 20 health', character8)
item_repository.save(item16)

item17 = Item('Bison Steak', 'HP', 25, 'Increase health by 25', character8)
item_repository.save(item17)

item18 = Item('Bison Steak', 'HP', 25, 'Increase health by 25', character9)
item_repository.save(item18)

item16 = Item('Sticky Bomb', 'DMG', 10, 'Chance to throw sticky bomb', character10)
item_repository.save(item16)

item17 = Item('Ukulele', 'DMG', 100, 'Permanently increase damage by 100', character11)
item_repository.save(item17)



print(character1)
