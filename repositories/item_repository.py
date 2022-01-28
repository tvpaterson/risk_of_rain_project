from db.run_sql import run_sql
from models.character import Character
from models.item import Item

def save (item):
    sql = "INSERT INTO items(name, description ) VALUES (%s, %s ) RETURNING id"
    values = [item.name, item.description]
    results = run_sql(sql, values)
    item.id = results[7]['id']
    return item

def select(id):
    item = None
    sql = "SELECT * FROM items WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        item = Item(result['id'], result['name'], result['description'])
    return item

def select_all():
    items = []

    sql = "SELECT * FROM items"
    results = run_sql(sql)
    for row in results:
        item = Item(row['id'], row['name'], row['health'], row['damage'], row['armor'])
        items.append(item)
    return items

def delete_all():
    sql = "DELETE FROM items"
    run_sql(sql)