from db.run_sql import run_sql
from models.character import Character
from models.item import Item
import repositories.character_repository as character_repository

import pdb

def save(item):
    sql = 'INSERT INTO items(name, attribute, value, description, character_id ) VALUES (%s, %s, %s, %s, %s ) RETURNING *'
    values = [item.name, item.attribute, item.value, item.description, item.character.id]
    results = run_sql(sql, values)
    item.id = results[0][0]
    return item

def select(id):
    item = None
    sql = "SELECT * FROM items WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        character = character_repository.select(result['character_id'])
        item = Item(result['name'], result['attribute'], result['value'], result['description'], character, result['id'])
    return item

def select_all():
    items = []

    sql = "SELECT * FROM items"
    results = run_sql(sql)
    for row in results:
        character = character_repository.select(row['character_id'])
        item = Item(row['name'], row['attribute'], row['value'], row['description'], character, row['id'])
        items.append(item)
    return items

def delete(id):
    sql = "DELETE FROM items WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM items"
    run_sql(sql)