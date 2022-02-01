from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.character import Character
import repositories.character_repository as character_repository
import repositories.item_repository as item_repository
import pdb

characters_blueprint = Blueprint("character", __name__)

@characters_blueprint.route("/characters")
def all_characters():
    characters = character_repository.select_all()
    return render_template("/characters/index.html", characters = characters)
    
@characters_blueprint.route("/characters/<id>", methods=["GET"])
def show_character(id):
    character = character_repository.select(id)
    character_items = character_repository.items(id)
    return render_template("characters/show.html", character = character, items = character_items)
    
@characters_blueprint.route("/characters/create", methods=["GET"])
def new_character():
    character = character_repository.select_all()
    return render_template("characters/create.html", character = character)

@characters_blueprint.route("/characters/<id>/edit/", methods=['GET'])
def edit_character(id):
    character = character_repository.select(id)
    return render_template("/characters/edit.html", character = character)


@characters_blueprint.route("/characters/<id>/update", methods=['POST'])
def update_character(id):
    name = request.form['character_name']
    health = request.form['character_health']
    damage = request.form['character_damage']
    armor = request.form['character_armor']
    character = Character(name, health, damage, armor, id)
    character_repository.update(character)
    return redirect('/characters')

@characters_blueprint.route("/characters", methods=['POST'])
def create_character():
    name = request.form['character_name']
    health = int(request.form['character_health'])
    damage = int(request.form['character_damage'])
    armor = int(request.form['character_armor'])
    new_character = Character(name, health, damage, armor)
    character_repository.save(new_character)
    return redirect("/characters")
    
@characters_blueprint.route("/characters/<id>/delete", methods=['POST'])
def delete_character(id):
    character_repository.delete(id)
    return redirect('/characters')

@characters_blueprint.route("/items/<id>/delete", methods=['POST'])
def delete_item(id):
    item_repository.delete(id)
    return redirect("/characters")
    