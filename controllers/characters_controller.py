from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.character import Character
import repositories.character_repository as character_repository

characters_blueprint = Blueprint("character", __name__)

@characters_blueprint.route("/characters")
def all_characters():
    characters = character_repository.select_all()
    return render_template("/characters/index.html", characters = characters)
    
@characters_blueprint.route("/characters/<id>", methods=["GET"])
def show_character(id):
    character = character_repository.select(id)
    return render_template("characters/show.html", character = character)
    
@characters_blueprint.route("/characters/create", methods=["GET"])
def new_character():
    character = character_repository.select_all()
    return render_template("characters/create.html", character = character)


@characters_blueprint.route("/characters", methods=['POST'])
def create_character():
    name = request.form['character_name']
    health = request.form['character_health']
    damage = request.form['character_damage']
    armor = request.form['character_armor']
    # id = request.form['character_id']
    new_character = Character(name, health, damage, armor)
    character_repository.save(new_character)
    return redirect("/characters")
    
@characters_blueprint.route("/characters/<id>/delete", methods=['POST'])
def delete_character(id):
    character_repository.delete(id)
    return redirect('/characters')

    