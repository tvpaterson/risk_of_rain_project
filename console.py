import pdb


import pdb
from models.character import Character
from models.item import Item
import repositories.character_repository as character_repository
import repositories.item_repository as item_repository

# character_repository.delete_all()
# item_repository.delete_all()

item7 = Item('Red Whip', 'Sprint faster when out of combat')
item_repository.save(item7)


print(item_repository.save(item7))


pdb.set_trace()