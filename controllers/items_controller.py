from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.item import Item
import repositories.item_repository as item_repository
import pdb

items_blueprint = Blueprint("item", __name__)

@items_blueprint.route("/items")
def all_items():
    items = item_repository.select_all()
    return render_template("/items/index.html", items = items)

@items_blueprint.route("/items/create")
def new_item():
    item = item_repository.select_all()
    return render_template("items/create.html", item = item)


@items_blueprint.route("/items", methods=['POST'])
def create_item():
    name = request.form['item_name']
    attribute = request.form['item_attribute']
    value = int(request.form['item_value'])
    description = request.form['item_description']
    new_item = Item(name, attribute, value, description)
    item_repository.save(new_item)
    return redirect("/items")

@items_blueprint.route("/items/<id>/delete", methods=['POST'])
def delete_item(id):
    item_repository.delete(id)
    return redirect('/items')
    
