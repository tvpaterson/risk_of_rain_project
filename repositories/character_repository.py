from db.run_sql import run_sql
from models.character import Character
from models.item import Item

def save (character):
    sql = "INSERT INTO users(name, health, damage, armor ) VALUES (%s, %s, %s, %s ) RETURNING id"
    values = [character.name]
    results = run_sql(sql, values)
    character.id = results[0]['id']
    return character

def select(id):
    character = None
    sql = "SELECT * FROM characters WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        character = Character(result['name'], result['health'], result['damage'], result['armor'], row['id'])
    return character

def select_all():
    characters = []

    sql = "SELECT * FROM characters"
    results = run_sql(sql)
    for row in results:
        character = Character(row['name'], row['health'], row['damage'], row['armor'], row['id'])
        characters.append(character)
    return characters

def delete_all():
    sql = "DELETE FROM characters"
    run_sql(sql)