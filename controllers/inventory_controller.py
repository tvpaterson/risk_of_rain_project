from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.character import Character
from models.inventory import Inventory
from models.item import Item
import repositories.character_repository as character_repository
import repositories.item_repository as item_repository
import repositories.inventory_repository as inventory_repository
import pdb

inventory_blueprint = Blueprint("inventory", __name__)

@inventory_blueprint.route("/characters")
def new_inventory():
    characters = character_repository.select_all()
    items = item_repository.select_all()
    return render_template("characters/create", character = characters, item = items)
