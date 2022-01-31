from db.run_sql import run_sql
from models.character import Character
from models.inventory import Inventory
from models.item import Item
import repositories.item_repository as item_repository
import repositories.character_repository as character_repository

import pdb

def save(inventory):
    sql = "INSERT INTO inventory ( character_id, item_id ) VALUES ( %s, %s ) RETURNING id"
    values = [inventory.character.id, inventory.item.id]
    results = run_sql( sql, values )
    inventory.id = results[0]['id']
    return inventory

def select_all():
    items = []

    sql = "SELECT * FROM inventories"
    results = run_sql(sql)

    for row in results:
        character = character_repository.select(row['character_id'])
        item = item_repository.select(row['item_id'])
        inventory = Inventory(character, item, row['id'])
        items.append(inventory)
    return items

