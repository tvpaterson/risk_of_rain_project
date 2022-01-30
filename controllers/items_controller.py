from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.item import Item
import repositories.item_repository as item_repository

items_blueprint = Blueprint("character", __name__)

@items_blueprint.route("/items")
def character_page():
    items = item_repository.select_all()
    return render_template("/items/index.html", items = items)
    
