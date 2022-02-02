from db.run_sql import run_sql
from models.character import Character
from models.item import Item
import pdb

def save(character):
    sql = 'INSERT INTO characters (name, health, damage, armor ) VALUES (%s, %s, %s, %s ) RETURNING id'
    values = [character.name, character.health, character.damage, character.armor]
    results = run_sql(sql, values)
    character.id = results[0]['id']
    return character


def select(id):
    character = None
    sql = "SELECT * FROM characters WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        character = Character(result['name'], result['health'], result['damage'], result['armor'], result['id'])
    return character

def select_all():
    characters = []

    sql = "SELECT * FROM characters"
    results = run_sql(sql)
    for row in results:
        character = Character(row['name'], row['health'], row['damage'], row['armor'], row['id'])
        characters.append(character)
    return characters

def update(character):
    sql = "UPDATE characters SET (name, health, damage, armor) = (%s, %s, %s, %s) WHERE id = %s"
    values = [character.name, character.health, character.damage, character.armor, character.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM characters WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM characters"
    run_sql(sql)

def items(id):
    items = []
    sql = "SELECT * FROM items WHERE character_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        character = select(id)
        item = Item(result['name'], result['attribute'], result['value'], result['description'], character, result['id'])
        items.append(item)
    return items
